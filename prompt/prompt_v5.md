# Prompt V5

## 实验目的

模拟 RAG（Retrieval-Augmented Generation）的基本流程，通过人为提供知识上下文，对比 AI 在有无知识支持情况下的回答质量。

---

## 实验一：无知识上下文

### Prompt

Docker Compose 是什么？

---

### AI 输出

# Docker Compose 是什么？

## ① 定义

**Docker Compose** 是 Docker 官方提供的**多容器应用编排工具**，用于通过一个配置文件（`docker-compose.yml` 或 `compose.yaml`）统一定义、启动、停止和管理多个 Docker 容器。

简单来说：

> **Docker 管理一个容器，Docker Compose 管理一组有关联的容器。**

例如，一个完整的网站通常包含：

* Web 服务（Nginx）
* 后端服务（Spring Boot / Flask）
* 数据库（MySQL）
* 缓存（Redis）

如果不用 Compose，需要手动启动多个容器，并且配置网络、端口、数据卷。

使用 Compose 后，只需要一条命令：

```bash
docker compose up -d
```

整个应用就会自动启动。

---

## ② 为什么需要 Docker Compose

假设你部署一个 Flask + Redis 项目。

如果不用 Compose：

```bash
docker run -d --name redis redis

docker run -d \
-p 5000:5000 \
--link redis \
my-flask
```

需要：

* 手动创建容器
* 手动配置网络
* 手动指定依赖
* 手动启动顺序

如果项目有 5~10 个容器，管理会变得非常麻烦。

而使用 Docker Compose：

```yaml
services:
  web:
    build: .
    ports:
      - "5000:5000"

  redis:
    image: redis
```

启动：

```bash
docker compose up -d
```

停止：

```bash
docker compose down
```

整个项目只需一个配置文件即可完成管理。

---

## ③ Docker Compose 核心组成

一个 Compose 项目通常包含：

```
project/
│
├── compose.yaml
├── Dockerfile
├── app.py
└── requirements.txt
```

其中：

### （1）compose.yaml

用于定义整个项目有哪些服务。

例如：

```yaml
services:

  web:
    build: .
    ports:
      - "5000:5000"

  redis:
    image: redis
```

这里定义了两个服务：

* web
* redis

---

### （2）Service（服务）

Compose 中最重要的概念。

例如：

```yaml
services:
  mysql:
    image: mysql:8

  redis:
    image: redis

  nginx:
    image: nginx
```

这里有三个 Service：

* MySQL
* Redis
* Nginx

每一个 Service 最终都会启动一个或多个容器。

---

### （3）Network（网络）

Compose 默认会自动创建网络。

例如：

```
web
 │
 │
redis
```

web 可以直接访问：

```
redis:6379
```

而不用知道 Redis 的 IP 地址。

例如：

```python
host = "redis"
```

不用写：

```
192.168.xx.xx
```

容器之间通过**服务名**通信。

---

### （4）Volume（数据卷）

用于保存数据。

例如：

```yaml
volumes:
  mysql_data:
```

挂载：

```yaml
services:
  mysql:
    image: mysql

    volumes:
      - mysql_data:/var/lib/mysql
```

即使删除容器：

```bash
docker compose down
```

数据库数据仍然保留。

---

## ④ 实际应用（以 Flask + Redis 为例）

你的项目结构：

```
counter/
│
├── app.py
├── Dockerfile
├── compose.yaml
```

### Dockerfile

```dockerfile
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install flask redis

CMD ["python","app.py"]
```

---

### compose.yaml

```yaml
services:

  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - redis

  redis:
    image: redis
```

---

### 启动项目

```bash
docker compose up -d
```

Compose 会自动完成：

```
构建镜像
      ↓
创建网络
      ↓
启动 Redis
      ↓
启动 Flask
      ↓
连接两个容器
```

浏览器访问：

```
http://localhost:5000
```

即可看到运行结果。

---

## ⑤ 常用命令

| 命令                             | 作用         |
| ------------------------------ | ---------- |
| `docker compose up`            | 启动项目       |
| `docker compose up -d`         | 后台启动       |
| `docker compose down`          | 停止并删除容器、网络 |
| `docker compose stop`          | 停止容器（不删除）  |
| `docker compose start`         | 启动已停止的容器   |
| `docker compose restart`       | 重启服务       |
| `docker compose ps`            | 查看服务状态     |
| `docker compose logs`          | 查看日志       |
| `docker compose build`         | 构建镜像       |
| `docker compose pull`          | 拉取镜像       |
| `docker compose exec web bash` | 进入容器       |

---

## ⑥ 与 Docker 的区别

| Docker          | Docker Compose         |
| --------------- | ---------------------- |
| 管理单个容器          | 管理多个容器                 |
| 使用 `docker run` | 使用 `docker compose up` |
| 手动配置网络          | 自动创建网络                 |
| 手动启动多个服务        | 一键启动整个项目               |
| 适合简单容器          | 适合完整应用                 |

可以理解为：

* **Docker**：负责创建和运行**单个容器**。
* **Docker Compose**：负责组织和管理**多个相互协作的容器**。

---

## ⑦ 面试重点（⭐）

1. **Docker Compose 的作用是什么？**

   * 用于定义、部署和管理多个 Docker 容器，通过一个 `compose.yaml` 文件统一配置，一键启动整个应用。

2. **Docker 与 Docker Compose 有什么区别？**

   * Docker 管理单个容器；Docker Compose 管理多容器应用，能够自动处理网络、依赖关系和统一启动。

3. **Compose 文件中常见字段有哪些？**

   * `services`：定义服务。
   * `image`：指定镜像。
   * `build`：根据 Dockerfile 构建镜像。
   * `ports`：端口映射。
   * `volumes`：数据卷挂载。
   * `environment`：环境变量。
   * `depends_on`：定义服务启动依赖。
   * `networks`：自定义网络。

4. **`depends_on` 的作用是什么？**

   * 控制服务的启动顺序，例如让 Web 服务先等待 Redis 或 MySQL 启动。但它**不能保证**依赖服务已经完全就绪，只保证容器按顺序启动。

5. **为什么很多开发项目都使用 Docker Compose？**

   * 可以把 Web、数据库、缓存、消息队列等多个服务统一编排，开发、测试和部署环境保持一致，实现“一条命令启动整个项目”。

---

> **与你的项目关联：** 你简历中的 **Flask + Redis 计数器项目** 就是典型的 Docker Compose 应用场景：使用 `Dockerfile` 构建 Flask 镜像，再通过 `compose.yaml` 同时启动 Flask 和 Redis 两个服务，并让它们通过同一网络通信。这类项目也是云计算和运维实习面试中非常常见的考察内容。


---

## 实验二：提供知识上下文

### Prompt

请严格依据下面提供的知识回答，不要补充未提供的信息。

【知识】

Docker Compose 是 Docker 官方提供的多容器编排工具。

开发者通过 docker-compose.yml

统一定义：

- Web
- MySQL
- Redis
- Nginx

执行 docker compose up 即可一次启动全部服务。

【结束】

问题：

Docker Compose 是什么？

---

### AI 输出

Docker Compose 是 **Docker 官方提供的多容器编排工具**。

开发者通过 `docker-compose.yml` 统一定义 Web、MySQL、Redis、Nginx 等服务，执行 `docker compose up` 即可一次启动全部服务。

## 输出效果分析

### 本次优化内容

本轮实验增加了外部知识作为上下文，模拟了 RAG 中"检索→增强→生成"的流程。

相比 V4，本次 Prompt 不再仅依赖模型已有知识，而是通过提供指定知识，引导模型基于给定内容生成回答。

---

### 输出效果

实验发现：

- 无知识上下文时，AI 依赖自身已有知识进行回答，虽然基本正确，但容易加入额外信息，回答风格也可能因模型不同而变化。

- 提供知识上下文后，AI 回答更加稳定，能够围绕指定知识生成内容，减少了无关信息，提高了回答的一致性和可控性。

---

### 与 V4 对比

| 对比项 | V4 | V5 |
|--------|----|----|
| Role | ✅ | ✅ |
| Context | ✅ | ✅ |
| Few-shot | ✅ | ✅ |
| 外部知识 | ❌ | ✅ |
| 回答准确性 | 较高 | 更高 |
| 幻觉风险 | 存在 | 降低 |
| 企业应用价值 | 中等 | 高 |

---

### 本轮结论

通过人为提供知识上下文，可以模拟 RAG 的基本工作方式，使模型基于指定知识回答问题，而不是完全依赖参数中的已有知识。这种方式能够提高回答的准确性、稳定性和可控性，也是企业构建 AI 知识库系统的核心思想。