#!/bin/bash

# DeepWiki Docker 构建脚本
# 在安装Docker Desktop后运行此脚本

echo "🚀 开始构建 DeepWiki Docker 镜像..."

# 检查Docker是否可用
if ! command -v docker &> /dev/null; then
    echo "❌ Docker 未安装或未启动"
    echo "请先安装 Docker Desktop："
    echo "1. 访问 https://www.docker.com/products/docker-desktop/"
    echo "2. 下载并安装 Docker Desktop"
    echo "3. 启动 Docker Desktop"
    echo "4. 重新运行此脚本"
    exit 1
fi

# 检查Docker守护进程是否运行
if ! docker info &> /dev/null; then
    echo "❌ Docker 守护进程未运行"
    echo "请启动 Docker Desktop 并等待它完全启动"
    exit 1
fi

echo "✅ Docker 已安装并运行"

# 构建镜像
echo "📦 构建 Docker 镜像..."
docker build -t deepwiki-open .

if [ $? -eq 0 ]; then
    echo "✅ Docker 镜像构建成功！"
    echo ""
    echo "🎉 下一步："
    echo "1. 配置环境变量："
    echo "   cp env.example .env"
    echo "   # 编辑 .env 文件，配置您的 API 密钥"
    echo ""
    echo "2. 启动应用："
    echo "   docker-compose up -d"
    echo ""
    echo "3. 访问应用："
    echo "   前端：http://localhost:3000"
    echo "   后端：http://localhost:8001"
else
    echo "❌ Docker 镜像构建失败"
    exit 1
fi
