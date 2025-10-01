# DeepWiki Docker 设置总结

## 🎯 已完成的工作

### 1. ✅ 优化的 Dockerfile
- 使用多阶段构建减少镜像大小
- 使用 uv 包管理器替代 pip，提高构建性能
- 包含完整的 Node.js 和 Python 环境
- 优化的启动脚本和进程管理

### 2. ✅ 完整的部署文档
- `DEPLOYMENT.md` - 详细部署指南
- `DOCKER_INSTALL.md` - Docker 安装指南
- `QUICK_START.md` - 快速启动指南

### 3. ✅ 环境配置
- `env.example` - 环境变量模板
- 包含所有必需的 API 密钥配置

### 4. ✅ 自动化脚本
- `build.sh` - 自动构建脚本
- 包含 Docker 环境检查和构建验证

## 🚀 快速开始

### 步骤 1: 安装 Docker Desktop

按照 `DOCKER_INSTALL.md` 中的说明安装 Docker Desktop。

### 步骤 2: 构建镜像

```bash
# 运行构建脚本
./build.sh

# 或者手动构建
docker build -t deepwiki-open .
```

### 步骤 3: 配置环境变量

```bash
# 复制环境变量模板
cp env.example .env

# 编辑 .env 文件，配置您的 API 密钥
# 至少配置以下一个 API 密钥：
# - GOOGLE_API_KEY
# - OPENAI_API_KEY
```

### 步骤 4: 启动应用

```bash
# 使用 Docker Compose 启动
docker-compose up -d

# 查看服务状态
docker-compose ps

# 查看日志
docker-compose logs -f
```

### 步骤 5: 访问应用

- **前端界面**: http://localhost:3000
- **后端 API**: http://localhost:8001

## 🔧 技术特点

### 多阶段构建
- **Node.js 阶段**: 构建 Next.js 前端应用
- **Python 阶段**: 安装 Python 依赖
- **最终镜像**: 包含所有运行时依赖

### 性能优化
- 使用 uv 包管理器，构建速度更快
- 优化的缓存层，减少重复构建
- 最小化镜像大小

### 稳定性
- 改进的启动脚本和进程管理
- 健康检查机制
- 优雅的关闭处理

### 数据持久化
- 自动保存仓库数据到 `~/.adalflow`
- 日志文件持久化
- 配置数据持久化

## 📁 文件结构

```
deepwiki-open/
├── Dockerfile              # 优化的 Docker 构建文件
├── docker-compose.yml      # Docker Compose 配置
├── build.sh               # 自动构建脚本
├── env.example            # 环境变量模板
├── DEPLOYMENT.md          # 详细部署指南
├── DOCKER_INSTALL.md      # Docker 安装指南
├── QUICK_START.md         # 快速启动指南
└── DOCKER_SETUP_SUMMARY.md # 本文件
```

## 🛠️ 故障排除

### 常见问题

1. **Docker 未安装**
   - 运行 `./build.sh` 检查 Docker 状态
   - 按照 `DOCKER_INSTALL.md` 安装 Docker Desktop

2. **端口冲突**
   - 修改 `.env` 文件中的 `PORT` 变量
   - 更新 `docker-compose.yml` 中的端口映射

3. **内存不足**
   - 在 Docker Desktop 设置中增加内存分配
   - 建议设置为 6GB 或更高

4. **API 密钥错误**
   - 检查 `.env` 文件中的 API 密钥格式
   - 确保 API 密钥有足够的配额

### 日志查看

```bash
# 查看所有服务日志
docker-compose logs

# 查看特定服务日志
docker-compose logs deepwiki

# 实时查看日志
docker-compose logs -f
```

## 🔄 更新应用

```bash
# 拉取最新代码
git pull

# 重新构建并重启
docker-compose up -d --build
```

## 🗑️ 完全卸载

```bash
# 停止并删除容器
docker-compose down -v

# 删除镜像
docker rmi deepwiki-open

# 删除持久化数据（可选）
rm -rf ~/.adalflow
```

## 🎉 总结

现在您的 DeepWiki 项目已经完全容器化，可以：

- ✅ 在任何支持 Docker 的环境中部署
- ✅ 无需安装额外的依赖
- ✅ 自动处理 Python 版本兼容性
- ✅ 数据持久化，重启不丢失
- ✅ 一键启动和停止

只需安装 Docker Desktop，然后运行 `./build.sh` 即可开始使用！
