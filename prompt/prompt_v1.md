# Prompt V1

## 实验目的

测试最基础 Prompt 的输出效果。

---

## Prompt

介绍 Docker。

---

## AI 输出

# Docker 介绍

## ① 什么是 Docker（定义）

Docker 是一个**开源的容器化平台（Container Platform）**，用于将应用程序及其运行环境打包成一个独立的**容器（Container）**，实现"**一次构建，到处运行（Build Once, Run Anywhere）**"。

简单理解：

> Docker = 一个轻量级的"软件打包箱"。

无论你的程序运行在：

* Windows
* Linux
* 云服务器
* 虚拟机

只要安装了 Docker，都可以直接运行，不需要重新配置环境。

---

## ② 为什么需要 Docker

在 Docker 出现之前，经常会遇到这样的问题：

```
开发：
我的电脑运行没问题啊！

测试：
为什么到测试服务器就报错？

运维：
服务器环境和开发环境不一样。

开发：
……
```

这就是经典的问题：

> **"在我电脑上能跑（It works on my machine）"**

原因包括：

* Python版本不同
* Java版本不同
* 缺少依赖
* 系统环境不同
* 配置文件不同

Docker 可以把：

```
应用程序
+
运行环境
+
依赖库
+
配置文件
```

全部一起打包。

因此：

无论在哪里运行，环境都完全一致。

---

## ③ Docker 的核心组件

### 1. Image（镜像）

镜像就是：

> 应用程序的模板。

里面包含：

* 操作系统
* 软件
* 环境
* 配置
* 依赖

例如：

```
Ubuntu
+
Python3.11
+
Flask
+
你的项目
```

这就是一个 Docker Image。

镜像类似：

```
安装光盘
```

不能直接修改。

---

### 2. Container（容器）

容器就是：

> 镜像运行后的实例。

关系：

```
镜像(Image)

↓

启动

↓

容器(Container)
```

例如：

```
Image：

python:3.11
```

运行：

```bash
docker run python:3.11
```

就得到一个容器。

可以同时启动很多个：

```
Container1

Container2

Container3
```

互不影响。

---

### 3. Docker Engine

Docker Engine 是 Docker 的核心。

负责：

* 创建容器
* 删除容器
* 下载镜像
* 管理镜像
* 网络管理
* 存储管理

常见命令：

```bash
docker run
docker stop
docker rm
docker images
docker ps
```

---

### 4. Docker Hub

Docker Hub 就像：

> Docker 的应用商店。

官方提供大量镜像：

例如：

```
Ubuntu

Nginx

MySQL

Redis

Python

Node

MongoDB
```

下载：

```bash
docker pull nginx
```

即可使用。

---

### 5. Dockerfile

Dockerfile 用来：

> 描述如何制作一个镜像。

例如：

```dockerfile
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python","app.py"]
```

然后：

```bash
docker build -t myapp .
```

即可生成自己的镜像。

---

### 6. Docker Compose

多个容器一起运行时：

例如：

```
网站

↓

需要

↓

MySQL

↓

Redis

↓

Nginx
```

可以使用 **Docker Compose**。

写一个：

```yaml
docker-compose.yml
```

例如：

```yaml
services:

  web:

    build: .

  mysql:

    image: mysql

  redis:

    image: redis
```

启动：

```bash
docker compose up
```

全部服务一起启动。

---

## ④ Docker 的实际应用

### 1. Web 项目部署

例如：

```
Flask

↓

Docker

↓

云服务器
```

任何服务器都能运行。

---

### 2. 微服务部署

例如：

```
用户服务

订单服务

商品服务
```

每个服务都是：

```
一个 Docker 容器
```

方便独立部署。

---

### 3. 数据库部署

例如：

```bash
docker run mysql
```

一分钟即可启动数据库。

无需安装。

---

### 4. CI/CD 自动部署

开发提交代码：

```
Git

↓

Jenkins

↓

Docker Build

↓

Docker Image

↓

部署服务器
```

整个过程自动完成。

---

### 5. 云计算平台

现在几乎所有云平台：

* 华为云
* 阿里云
* 腾讯云
* AWS

都大量使用 Docker。

后续再配合 Kubernetes（K8s）实现：

* 自动扩容
* 自动恢复
* 自动部署

---

## ⑤ Docker 与虚拟机的区别

| 对比项       | Docker | 虚拟机（VM） |
| --------- | ------ | ------- |
| 启动速度      | 秒级     | 分钟级     |
| 占用空间      | MB 级   | GB 级    |
| 是否共享宿主机内核 | 是      | 否       |
| 性能        | 接近原生   | 有一定损耗   |
| 部署速度      | 快      | 较慢      |

示意图：

### 虚拟机

```
硬件

↓

宿主机OS

↓

Hypervisor

↓

Guest OS

↓

App
```

每台虚拟机都有自己的操作系统，因此资源占用较大。

---

### Docker

```
硬件

↓

宿主机OS

↓

Docker Engine

↓

Container

↓

App
```

容器共享宿主机内核，因此更加轻量、高效。

---

## 面试重点（高频）

### 1. Docker 是什么？

> Docker 是一个容器化平台，用于将应用程序及其依赖打包成镜像，并以容器形式运行，保证环境一致性，实现快速部署和交付。

---

### 2. Docker 的优势有哪些？

* 环境一致
* 部署快速
* 资源占用少
* 易于迁移
* 支持微服务
* 便于 CI/CD 自动化部署

---

### 3. Image 和 Container 有什么区别？

**Image（镜像）**：

* 静态模板
* 不运行
* 不可直接修改

**Container（容器）**：

* 镜像运行后的实例
* 可以启动、停止、删除
* 可以同时运行多个容器

---

### 4. Dockerfile 的作用是什么？

Dockerfile 用于定义构建镜像的步骤，例如选择基础镜像、复制代码、安装依赖、设置启动命令，实现镜像构建自动化。

---

### 5. Docker Compose 的作用是什么？

Docker Compose 用于编排多个容器，通过一个 `docker-compose.yml` 文件统一管理多个服务（如 Web、MySQL、Redis），一条命令即可完成启动、停止和管理。

---




---

## 输出效果分析

### 优点

-

### 缺点

-

### 改进方向

-

## 输出效果分析

### 优点

- 能够正确介绍 Docker 的基本概念和核心组件。
- 内容准确，覆盖了 Docker 的主要知识点。
- 输出速度快，可作为初步学习资料。

### 缺点

- Prompt 只有"介绍 Docker"一句话，没有指定角色、目标读者和使用场景。
- AI 自行决定输出内容，重点不够明确。
- 虽然有一定结构，但没有针对实际需求进行定制。
- 内容偏理论，缺少针对面试、学习路线或实践案例的侧重。
- 输出格式不可控，不同模型或不同时间生成的内容可能存在较大差异，可复现性较低。

### 存在的问题

本次 Prompt 属于开放式提问，缺乏明确约束，AI 需要自行推测用户意图，因此回答虽然完整，但针对性不足，难以满足特定场景（如课程开发、技术文档整理或知识库构建）的需求。

### 改进方向

下一轮 Prompt 将加入以下优化策略：

1. 增加角色设定（Role）
   - 指定 AI 扮演云计算讲师，提高专业性。

2. 明确目标读者（Audience）
   - 面向网络工程专业学生，控制知识深度。

3. 增加输出约束（Constraint）
   - 指定 Markdown 格式。
   - 指定章节结构。
   - 限制回答长度。

4. 增加输出目标（Goal）
   - 增加面试重点总结。
   - 增加知识点归纳。
   - 提高文档结构化程度。

### 本轮实验结论

仅使用简单 Prompt 即可获得正确答案，但回答的结构化程度和可控性较低。通过增加角色设定、输出约束和目标要求，预计可以进一步提升回答质量，这也是下一轮 Prompt 优化的重点。