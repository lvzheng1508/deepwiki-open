# Docker 安装指南

由于当前系统环境存在权限问题，请按照以下步骤手动安装 Docker Desktop：

## 方法一：手动下载安装（推荐）

### 1. 下载 Docker Desktop

访问 Docker 官方网站下载最新版本：
https://www.docker.com/products/docker-desktop/

或者直接下载链接：
https://desktop.docker.com/mac/main/amd64/Docker%20Desktop.dmg

### 2. 安装 Docker Desktop

```bash
# 打开下载的 .dmg 文件
open Docker\ Desktop.dmg

# 将 Docker 图标拖拽到 Applications 文件夹
```

### 3. 启动 Docker Desktop

```bash
# 从 Applications 文件夹启动 Docker Desktop
open -a "Docker Desktop"

# 或者通过命令行启动
open /Applications/Docker.app
```

### 4. 完成初始设置

- 首次启动时，Docker Desktop 会请求系统权限
- 同意所有权限请求
- 等待 Docker 守护进程启动完成

## 方法二：使用 Homebrew（如果权限问题已解决）

```bash
# 清理现有的 Docker 安装
brew uninstall --force docker docker-compose

# 安装 Docker Desktop
brew install --cask docker

# 启动 Docker Desktop
open -a "Docker Desktop"
```

## 验证安装

安装完成后，验证 Docker 是否正常工作：

```bash
# 检查 Docker 版本
docker --version

# 检查 Docker Compose 版本
docker compose version

# 运行测试容器
docker run hello-world
```

## 配置 Docker

### 1. 调整资源限制

在 Docker Desktop 设置中：
- 内存：建议设置为 6GB 或更高
- CPU：建议设置为 4 核心或更高
- 磁盘：确保有足够的磁盘空间

### 2. 启用 Kubernetes（可选）

如果需要 Kubernetes 支持，可以在设置中启用。

## 故障排除

### 常见问题

1. **权限问题**
   - 确保 Docker Desktop 有完整的磁盘访问权限
   - 在系统设置中检查权限设置

2. **启动失败**
   - 重启 Docker Desktop
   - 重启计算机
   - 检查系统日志

3. **网络问题**
   - 检查防火墙设置
   - 确保网络连接正常

### 重置 Docker

如果遇到问题，可以重置 Docker Desktop：

1. 点击 Docker Desktop 菜单栏图标
2. 选择 "Troubleshoot"
3. 点击 "Reset to factory defaults"

## 安装完成后

Docker 安装完成后，您可以返回项目根目录并运行：

```bash
# 构建 DeepWiki Docker 镜像
docker build -t deepwiki-open .

# 或者使用 Docker Compose
docker-compose up -d
```

## 系统要求

- macOS 10.15 或更高版本
- 至少 4GB 可用内存（建议 8GB+）
- 至少 2GB 可用磁盘空间
