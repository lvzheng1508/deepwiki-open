# DeepWiki Docker 部署指南

本文档详细说明如何使用 Docker 部署 DeepWiki 项目。

## 前提条件

- 已安装 Docker 和 Docker Compose
- 至少 6GB 可用内存
- 至少 2GB 可用磁盘空间

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/AsyncFuncAI/deepwiki-open.git
cd deepwiki-open
```

### 2. 配置环境变量

复制环境变量模板并配置您的 API 密钥：

```bash
cp env.example .env
```

编辑 `.env` 文件，至少配置以下必需的 API 密钥之一：

```bash
# 至少配置以下一个 API 密钥
GOOGLE_API_KEY=your_google_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. 使用 Docker Compose 启动

```bash
docker-compose up -d
```

### 4. 访问应用

- 前端界面: http://localhost:3000
- 后端 API: http://localhost:8001

## 详细部署步骤

### 构建自定义镜像

如果您需要自定义构建镜像：

```bash
# 构建镜像
docker build -t deepwiki-open .

# 运行容器
docker run -d \
  --name deepwiki \
  -p 8001:8001 \
  -p 3000:3000 \
  --env-file .env \
  -v ~/.adalflow:/root/.adalflow \
  deepwiki-open
```

### 环境变量说明

#### 必需的环境变量

至少需要配置以下一个 API 密钥：

- `GOOGLE_API_KEY`: Google Gemini API 密钥
- `OPENAI_API_KEY`: OpenAI API 密钥

#### 可选的环境变量

- `OPENAI_BASE_URL`: 第三方 OpenAI 兼容端点
- `OPENAI_MODEL`: 默认模型名称
- `OPENROUTER_API_KEY`: OpenRouter API 密钥
- `AZURE_OPENAI_API_KEY`: Azure OpenAI API 密钥
- `AZURE_OPENAI_ENDPOINT`: Azure OpenAI 端点
- `AZURE_OPENAI_VERSION`: Azure OpenAI 版本
- `OLLAMA_HOST`: Ollama 主机地址
- `PORT`: API 服务器端口 (默认: 8001)
- `SERVER_BASE_URL`: API 服务器基础 URL
- `LOG_LEVEL`: 日志级别 (默认: INFO)
- `LOG_FILE_PATH`: 日志文件路径

### 数据持久化

容器会自动将以下数据持久化到主机：

- `~/.adalflow/repos/`: 克隆的代码仓库
- `~/.adalflow/databases/`: 向量数据库和嵌入
- `~/.adalflow/wikicache/`: 生成的 wiki 缓存
- `./api/logs/`: 应用程序日志

### 健康检查

容器包含健康检查，可以通过以下命令验证服务状态：

```bash
# 检查容器状态
docker-compose ps

# 检查健康状态
docker inspect --format='{{.State.Health.Status}}' deepwiki-open-deepwiki-1

# 查看日志
docker-compose logs -f
```

## 故障排除

### 常见问题

1. **端口冲突**
   - 修改 `.env` 文件中的 `PORT` 变量
   - 更新 `docker-compose.yml` 中的端口映射

2. **内存不足**
   - 确保系统有足够内存 (建议 6GB+)
   - 在 `docker-compose.yml` 中调整内存限制

3. **API 密钥错误**
   - 检查 `.env` 文件中的 API 密钥格式
   - 确保 API 密钥有足够的配额

4. **构建失败**
   - 清理 Docker 缓存: `docker system prune -f`
   - 重新构建: `docker-compose build --no-cache`

### 日志查看

```bash
# 查看所有服务日志
docker-compose logs

# 查看特定服务日志
docker-compose logs deepwiki

# 实时查看日志
docker-compose logs -f
```

### 重启服务

```bash
# 重启所有服务
docker-compose restart

# 重启特定服务
docker-compose restart deepwiki
```

## 生产环境部署

### 使用环境变量

在生产环境中，建议使用环境变量而非 `.env` 文件：

```bash
docker run -d \
  --name deepwiki \
  -p 8001:8001 \
  -p 3000:3000 \
  -e GOOGLE_API_KEY=your_key \
  -e OPENAI_API_KEY=your_key \
  -v ~/.adalflow:/root/.adalflow \
  deepwiki-open
```

### 使用 Docker Swarm

```yaml
version: '3.8'
services:
  deepwiki:
    image: deepwiki-open:latest
    ports:
      - "8001:8001"
      - "3000:3000"
    environment:
      - GOOGLE_API_KEY=${GOOGLE_API_KEY}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    volumes:
      - deepwiki_data:/root/.adalflow
    deploy:
      replicas: 1
      resources:
        limits:
          memory: 6G
        reservations:
          memory: 2G

volumes:
  deepwiki_data:
```

## 性能优化

### 资源限制

建议为容器分配：
- 内存: 6GB (限制) / 2GB (保留)
- CPU: 2-4 核心

### 缓存优化

- 使用 SSD 存储以获得更好的 I/O 性能
- 定期清理旧的缓存数据
- 监控磁盘使用情况

## 安全考虑

- 定期更新 API 密钥
- 使用强密码保护访问
- 监控日志中的异常活动
- 限制对 API 端点的访问

## 更新应用

```bash
# 拉取最新代码
git pull

# 重新构建镜像
docker-compose build

# 重启服务
docker-compose up -d
```

## 卸载

```bash
# 停止并删除容器
docker-compose down

# 删除镜像
docker rmi deepwiki-open

# 删除持久化数据 (可选)
rm -rf ~/.adalflow
```
