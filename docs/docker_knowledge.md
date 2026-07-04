# Docker知识库

## Docker

### 定义

Docker 是一个开源容器平台，用于将应用程序及其运行环境打包成镜像，并以容器形式运行，实现环境一致性。

### 作用

- 保证开发、测试、生产环境一致
- 提高部署效率
- 支持快速迁移
- 支持微服务架构

### 核心特点

- 轻量级
- 秒级启动
- 环境隔离
- 易于扩展

### 常见命令

```bash
docker run
docker ps
docker images
docker stop
```

### 面试重点

Docker 的核心思想是什么？

Docker 与虚拟机有什么区别？

Docker 为什么比虚拟机快？

## Docker Compose

### 定义

Docker Compose 是 Docker 官方提供的多容器编排工具。

### 作用

统一管理多个容器。

### 核心特点

- 一个YAML文件管理全部服务
- 一键启动
- 一键停止
- 配置简单

### 常用命令

```bash
docker compose up

docker compose down
```

### 面试重点

Docker Compose 与 Dockerfile 有什么区别？

什么时候使用 Compose？