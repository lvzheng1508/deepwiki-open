# Build argument for custom certificates directory
ARG CUSTOM_CERT_DIR="certs"

FROM node:20-alpine3.22 AS node_base

FROM node_base AS node_deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --legacy-peer-deps

FROM node_base AS node_builder
WORKDIR /app
COPY --from=node_deps /app/node_modules ./node_modules
# Copy only necessary files for Next.js build
COPY package.json package-lock.json next.config.ts tsconfig.json tailwind.config.js postcss.config.mjs ./
COPY src/ ./src/
COPY public/ ./public/
# Increase Node.js memory limit for build and disable telemetry
ENV NODE_OPTIONS="--max-old-space-size=4096"
ENV NEXT_TELEMETRY_DISABLED=1
RUN NODE_ENV=production npm run build

FROM python:3.11-slim AS py_deps
WORKDIR /app
# Install uv for faster Python dependency management
RUN pip install uv
# Copy Python project files
COPY pyproject.toml uv.lock ./
# Install dependencies using uv
RUN uv sync --frozen --no-dev

# Use Python 3.11 as final image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install Node.js and npm
RUN apt-get update && apt-get install -y \
  curl \
  gnupg \
  git \
  ca-certificates \
  && mkdir -p /etc/apt/keyrings \
  && curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg \
  && echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_20.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list \
  && apt-get update \
  && apt-get install -y nodejs \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Update certificates if custom ones were provided and copied successfully
RUN if [ -n "${CUSTOM_CERT_DIR}" ]; then \
  mkdir -p /usr/local/share/ca-certificates && \
  if [ -d "${CUSTOM_CERT_DIR}" ]; then \
  cp -r ${CUSTOM_CERT_DIR}/* /usr/local/share/ca-certificates/ 2>/dev/null || true; \
  update-ca-certificates; \
  echo "Custom certificates installed successfully."; \
  else \
  echo "Warning: ${CUSTOM_CERT_DIR} not found. Skipping certificate installation."; \
  fi \
  fi

# Copy Python dependencies from uv installation
COPY --from=py_deps /app/.venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy Python source code
COPY api/ ./api/

# Copy Node app
COPY --from=node_builder /app/public ./public
COPY --from=node_builder /app/.next/standalone ./
COPY --from=node_builder /app/.next/static ./.next/static

# Expose the port the app runs on
EXPOSE ${PORT:-8001} 3000

# Create a script to run both backend and frontend
RUN echo '#!/bin/bash\n\
  set -e\n\
  \n\
  # Load environment variables from .env file if it exists\n\
  if [ -f .env ]; then\n\
  export $(grep -v "^#" .env | xargs -r)\n\
  fi\n\
  \n\
  # Check for required environment variables\n\
  if [ -z "$OPENAI_API_KEY" ] && [ -z "$GOOGLE_API_KEY" ]; then\n\
  echo "Warning: Neither OPENAI_API_KEY nor GOOGLE_API_KEY environment variables are set."\n\
  echo "At least one of these is required for DeepWiki to function properly."\n\
  echo "You can provide them via a mounted .env file or as environment variables when running the container."\n\
  fi\n\
  \n\
  # Set default port if not provided\n\
  PORT=${PORT:-8001}\n\
  \n\
  # Function to handle cleanup\n\
  cleanup() {\n\
  echo "Shutting down services..."\n\
  kill $BACKEND_PID $FRONTEND_PID 2>/dev/null || true\n\
  wait\n\
  echo "Services stopped."\n\
  }\n\
  \n\
  # Set trap for cleanup\n\
  trap cleanup SIGTERM SIGINT\n\
  \n\
  # Start the API server in the background\n\
  echo "Starting backend API server on port $PORT..."\n\
  python -m api.main --port $PORT &\n\
  BACKEND_PID=$!\n\
  \n\
  # Wait a moment for backend to start\n\
  sleep 3\n\
  \n\
  # Start the frontend server\n\
  echo "Starting frontend server on port 3000..."\n\
  PORT=3000 HOSTNAME=0.0.0.0 node server.js &\n\
  FRONTEND_PID=$!\n\
  \n\
  # Wait for any process to exit\n\
  wait -n\n\
  \n\
  # If we reach here, one of the processes has exited\n\
  echo "One of the services has stopped. Shutting down..."\n\
  cleanup\n\
  exit 1' > /app/start.sh && chmod +x /app/start.sh

# Set environment variables
ENV PORT=8001
ENV NODE_ENV=production
ENV SERVER_BASE_URL=http://localhost:${PORT:-8001}

# Create empty .env file (will be overridden if one exists at runtime)
RUN touch .env

# Command to run the application
CMD ["/app/start.sh"]
