# Docker 官方知识（整理版）

## Docker

Docker 是一个开源容器平台。

它可以将应用程序及运行环境一起打包成镜像，并以容器方式运行。

---

## Docker Image

Image（镜像）是容器运行的基础模板。

镜像包含：

- 操作系统
- 应用程序
- 配置
- 依赖

---

## Docker Container

Container（容器）是镜像运行后的实例。

一个镜像可以启动多个容器。

---

## Docker Compose

Docker Compose 是 Docker 官方提供的多容器编排工具。

开发者通过 docker-compose.yml

统一定义：

- Web
- MySQL
- Redis
- Nginx

执行

docker compose up

即可启动全部服务。

---

## Dockerfile

Dockerfile 用于描述镜像构建过程。

通过 Dockerfile 可以自动构建 Docker Image。