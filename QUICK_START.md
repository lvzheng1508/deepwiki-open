# DeepWiki 快速启动指南

## 前提条件

- 已安装 Docker Desktop
- 至少 6GB 可用内存

## 快速部署步骤

### 1. 配置环境变量

```bash
# 复制环境变量模板
cp env.example .env

# 编辑 .env 文件，至少配置以下一个 API 密钥
# 使用您喜欢的编辑器编辑 .env 文件
```

在 `.env` 文件中，至少配置以下一个 API 密钥：

```bash
# Google Gemini API 密钥
GOOGLE_API_KEY=your_google_api_key_here

# 或 OpenAI API 密钥
OPENAI_API_KEY=your_openai_api_key_here
```

### 2. 使用 Docker Compose 启动

```bash
# 启动所有服务
docker-compose up -d

# 查看服务状态
docker-compose ps

# 查看实时日志
docker-compose logs -f
```

### 3. 访问应用

- **前端界面**: http://localhost:3000
- **后端 API**: http://localhost:8001

### 4. 停止服务

```bash
# 停止所有服务
docker-compose down

# 停止并删除数据（谨慎使用）
docker-compose down -v
```

## 手动构建和运行

如果您需要自定义构建：

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

## 验证部署

### 检查服务状态

```bash
# 检查容器状态
docker-compose ps

# 检查健康状态
docker inspect --format='{{.State.Health.Status}}' deepwiki-open-deepwiki-1

# 测试 API 端点
curl http://localhost:8001/health
```

### 查看日志

```bash
# 查看所有服务日志
docker-compose logs

# 查看特定服务日志
docker-compose logs deepwiki

# 实时查看日志
docker-compose logs -f
```

## 故障排除

### 常见问题

1. **端口冲突**
   ```bash
   # 修改 .env 文件中的 PORT 变量
   PORT=8002
   ```

2. **内存不足**
   - 在 Docker Desktop 设置中增加内存分配
   - 建议设置为 6GB 或更高

3. **API 密钥错误**
   - 检查 `.env` 文件中的 API 密钥格式
   - 确保 API 密钥有足够的配额

4. **构建失败**
   ```bash
   # 清理缓存并重新构建
   docker-compose build --no-cache
   ```

### 重启服务

```bash
# 重启所有服务
docker-compose restart

# 重新构建并重启
docker-compose up -d --build
```

## 数据持久化

容器会自动将以下数据持久化到主机：

- `~/.adalflow/repos/`: 克隆的代码仓库
- `~/.adalflow/databases/`: 向量数据库和嵌入
- `~/.adalflow/wikicache/`: 生成的 wiki 缓存
- `./api/logs/`: 应用程序日志

## 更新应用

```bash
# 拉取最新代码
git pull

# 重新构建并重启
docker-compose up -d --build
```

## 完全卸载

```bash
# 停止并删除容器
docker-compose down -v

# 删除镜像
docker rmi deepwiki-open

# 删除持久化数据（可选）
rm -rf ~/.adalflow
```

## 获取帮助

如果遇到问题，请查看：

- [DEPLOYMENT.md](./DEPLOYMENT.md) - 详细部署指南
- [DOCKER_INSTALL.md](./DOCKER_INSTALL.md) - Docker 安装指南
- 项目 README - 完整功能说明
