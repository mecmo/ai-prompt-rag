这次直接给你 **README.md 原文**，复制进去就是完整 README。

# Local RAG Knowledge QA Demo

一个基于本地 Markdown 知识库的简易 RAG 问答 Demo。

本项目用于演示一个最基础的本地知识库问答流程：
读取本地 Markdown 文档，将内容切分成多个文本块，根据用户问题检索相关内容，再把检索结果拼接进 Prompt 中交给大模型回答。

项目适合用于学习：

* RAG 基本流程
* Markdown 知识库读取
* 文本切分
* 简单相似度检索
* Prompt 构建
* 本地问答历史保存
* Python 项目模块化拆分

---

## 1. 项目简介

RAG，全称 Retrieval-Augmented Generation，即“检索增强生成”。

传统大模型只能依靠自身已有知识回答问题，而 RAG 会先从指定知识库中检索相关内容，再让大模型基于这些内容进行回答。

本项目的基本流程如下：

```text
用户输入问题
    ↓
读取本地 Markdown 知识库
    ↓
将知识库内容切分成多个文本块
    ↓
根据问题检索最相关的文本块
    ↓
构建 Prompt
    ↓
调用大模型生成回答
    ↓
保存问答历史
```

---

## 2. 项目功能

本项目实现了以下功能：

1. 读取本地 Markdown 知识库文件
2. 将 Markdown 文本切分成多个知识块
3. 根据用户问题进行相关内容检索
4. 自动构建适合大模型回答的 Prompt
5. 调用大模型生成回答
6. 支持命令行连续提问
7. 支持输入 `exit` 退出程序
8. 自动保存问答历史到 `history.md`

---

## 3. 项目目录结构

```text
local-rag-demo/
│
├── main.py              # 项目入口文件
├── config.py            # 配置文件
├── loader.py            # Markdown 文件读取模块
├── splitter.py          # 文本切分模块
├── retriever.py         # 检索模块
├── prompt_builder.py    # Prompt 构建模块
├── llm.py               # 大模型调用模块
├── history.py           # 问答历史保存模块
│
├── knowledge.md         # 本地知识库文件
├── history.md           # 问答历史记录文件，运行后自动生成
├── requirements.txt     # 项目依赖
└── README.md            # 项目说明文档
```

---

## 4. 环境要求

建议使用以下环境：

```text
Python 3.9+
VS Code
Windows / macOS / Linux
```

如果使用 VS Code，推荐安装以下插件：

* Python
* Pylance
* Markdown All in One

---

## 5. 安装依赖

进入项目目录后，执行：

```bash
pip install -r requirements.txt
```

如果当前项目暂时没有第三方依赖，也可以先创建一个空的 `requirements.txt` 文件，后续再根据需要补充。

---

## 6. 配置说明

项目中的主要配置放在 `config.py` 中。

示例：

```python
KNOWLEDGE_PATH = "knowledge.md"
TOP_K = 3
HISTORY_PATH = "history.md"
```

参数说明：

| 配置项              | 作用             |
| ---------------- | -------------- |
| `KNOWLEDGE_PATH` | 本地知识库文件路径      |
| `TOP_K`          | 每次检索返回的相关文本块数量 |
| `HISTORY_PATH`   | 问答历史保存文件路径     |

---

## 7. 知识库文件说明

知识库文件使用 Markdown 格式，默认文件名为：

```text
knowledge.md
```

示例内容：

```markdown
# Docker

Docker 是一种容器化技术，可以将应用程序及其依赖打包到容器中运行。

# Docker Compose

Docker Compose 是 Docker 官方提供的多容器编排工具。

开发者可以通过 docker-compose.yml 统一定义 Web、MySQL、Redis、Nginx 等服务。

执行 docker compose up 即可一次启动全部服务。
```

程序会读取该文件，并基于其中内容回答用户问题。

---

## 8. 运行项目

在项目根目录下执行：

```bash
python main.py
```

运行后，终端会显示：

```text
Local RAG Knowledge QA Demo
Type exit to quit
----------------------------------------
```

然后可以输入问题，例如：

```text
Question: Docker Compose 是什么？
```

如果知识库中存在相关内容，程序会检索相关文本块，并调用大模型生成回答。

输入以下内容可以退出程序：

```text
exit
```

---

## 9. 主程序说明

`main.py` 是整个项目的入口文件。

核心代码逻辑如下：

```python
from loader import load_markdown
from splitter import split_markdown
from retriever import retrieve
from prompt_builder import build_prompt
from llm import ask_llm
from config import KNOWLEDGE_PATH, TOP_K
from history import save_history

def main():
    text = load_markdown(KNOWLEDGE_PATH)
    chunks = split_markdown(text)

    print("Local RAG Knowledge QA Demo")
    print("Type exit to quit")
    print("-" * 40)

    while True:
        query = input("\nQuestion: ")

        if query.lower() == "exit":
            print("Program exited.")
            break

        results = retrieve(query, chunks, top_k=TOP_K)

        if not results:
            print("\nNo related information found in knowledge base.")
            continue

        contexts = [chunk for score, chunk in results]
        prompt = build_prompt(query, contexts)

        answer = ask_llm(prompt)

        print("\nAnswer:")
        print(answer)

        save_history(query, answer)

if __name__ == "__main__":
    main()
```

---

## 10. 各模块说明

### 10.1 loader.py

`loader.py` 负责读取本地 Markdown 知识库文件。

主要功能：

* 根据路径打开 Markdown 文件
* 读取文本内容
* 返回完整字符串

示例：

```python
def load_markdown(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
```

---

### 10.2 splitter.py

`splitter.py` 负责将 Markdown 文本切分成多个知识块。

主要功能：

* 按标题或段落切分文本
* 去除空白内容
* 返回文本块列表

示例：

```python
def split_markdown(text):
    chunks = text.split("\n\n")
    return [chunk.strip() for chunk in chunks if chunk.strip()]
```

---

### 10.3 retriever.py

`retriever.py` 负责根据用户问题检索相关知识块。

主要功能：

* 接收用户问题和知识块列表
* 计算问题与文本块的相关性
* 返回最相关的前 `top_k` 个文本块

示例：

```python
def retrieve(query, chunks, top_k=3):
    results = []

    for chunk in chunks:
        score = 0
        for word in query:
            if word in chunk:
                score += 1

        if score > 0:
            results.append((score, chunk))

    results.sort(key=lambda x: x[0], reverse=True)
    return results[:top_k]
```

---

### 10.4 prompt_builder.py

`prompt_builder.py` 负责构建发送给大模型的 Prompt。

主要功能：

* 将用户问题和检索到的知识块组合起来
* 限制大模型只能根据知识库回答
* 避免模型随意补充知识库外的信息

示例：

```python
def build_prompt(query, contexts):
    context_text = "\n\n".join(contexts)

    prompt = f"""
请严格根据下面提供的知识库内容回答问题。
如果知识库中没有相关信息，请回答：知识库中未找到相关内容。

【知识库内容】
{context_text}

【用户问题】
{query}

【回答】
"""
    return prompt
```

---

### 10.5 llm.py

`llm.py` 负责调用大模型接口，生成最终回答。

主要功能：

* 接收构建好的 Prompt
* 调用大模型
* 返回模型生成结果

如果当前阶段只是学习 RAG 流程，也可以先用模拟回答代替真实接口。

示例：

```python
def ask_llm(prompt):
    return "这里是大模型根据 Prompt 生成的回答。"
```

后续可以替换为真实的大模型 API 调用。

---

### 10.6 history.py

`history.py` 负责保存用户问题和模型回答。

主要功能：

* 将每次问答追加写入 `history.md`
* 方便后续查看测试记录
* 便于总结 Prompt 优化过程

示例：

```python
from config import HISTORY_PATH

def save_history(question, answer):
    with open(HISTORY_PATH, "a", encoding="utf-8") as f:
        f.write("## Question\n")
        f.write(question + "\n\n")
        f.write("## Answer\n")
        f.write(answer + "\n\n")
        f.write("---\n\n")
```

---

## 11. 问答历史说明

程序运行后，会自动生成或更新：

```text
history.md
```

示例内容：

```markdown
## Question
Docker Compose 是什么？

## Answer
Docker Compose 是 Docker 官方提供的多容器编排工具。开发者可以通过 docker-compose.yml 统一定义多个服务，并通过 docker compose up 一次启动全部服务。

---
```

通过 `history.md` 可以记录：

* 用户提出的问题
* 模型生成的回答
* Prompt 调试效果
* 不同版本回答的对比结果

这对于简历项目中的“Prompt 优化过程记录”和“输出结果对比测试”很有帮助。

---

## 12. 示例运行效果

终端输入：

```text
Question: Docker Compose 是什么？
```

程序输出：

```text
Answer:
Docker Compose 是 Docker 官方提供的多容器编排工具。开发者可以通过 docker-compose.yml 统一定义 Web、MySQL、Redis、Nginx 等服务，执行 docker compose up 即可一次启动全部服务。
```

如果知识库中没有相关内容，程序可能输出：

```text
No related information found in knowledge base.
```

---

## 13. 项目学习重点

通过本项目，可以掌握以下内容：

1. Python 项目的模块化拆分
2. Markdown 文档读取与处理
3. RAG 的基本工作流程
4. 知识库切分方法
5. 简单文本检索逻辑
6. Prompt 构建方式
7. 大模型问答流程
8. 问答历史保存
9. 项目运行测试与结果记录

---

## 14. 项目可优化方向

当前项目是一个基础版 Demo，后续可以继续优化：

### 14.1 优化文本切分方式

当前可以使用简单的段落切分，后续可以改成：

* 按 Markdown 标题切分
* 按固定字数切分
* 按语义段落切分
* 增加 chunk overlap 重叠内容

### 14.2 优化检索方式

当前可以使用简单关键词匹配，后续可以升级为：

* TF-IDF 检索
* BM25 检索
* 向量检索
* FAISS 本地向量库
* Embedding 语义相似度检索

### 14.3 优化 Prompt

可以尝试不同 Prompt 模板，例如：

* 严格依据知识库回答
* 不允许补充知识库外内容
* 输出 Markdown 格式
* 输出分点结构
* 输出面试风格回答
* 输出简短版和详细版

### 14.4 增加前端页面

后续可以使用以下方式增加交互界面：

* Streamlit
* Gradio
* Flask
* Django

### 14.5 接入真实大模型 API

当前如果使用模拟回答，可以后续替换为真实接口，例如：

* OpenAI API
* 通义千问 API
* 智谱 AI API
* DeepSeek API
* 本地 Ollama 模型

---
## 15. 常见问题

### 15.1 为什么要先检索再回答？

因为大模型本身不一定知道本地知识库中的内容。
通过先检索相关文本，再把内容放入 Prompt，可以让模型基于指定资料回答问题。

### 15.2 为什么要切分知识库？

如果知识库内容太长，直接全部放入 Prompt 会导致内容过多、成本变高、回答不准确。
切分后可以只选取和问题最相关的部分，提高回答质量。

### 15.3 为什么要保存 history.md？

保存历史可以用于：

* 查看测试记录
* 对比不同 Prompt 的回答效果
* 总结优化过程
* 作为项目成果证明

### 15.4 这个项目算 RAG 项目吗？

算是一个基础版 RAG Demo。

它具备 RAG 的核心流程：

```text
知识库读取 → 文本切分 → 检索 → Prompt 构建 → 大模型回答
```

虽然当前版本比较简单，但已经能体现 RAG 的基本思想。

---

## 16. 项目总结

本项目完成了一个基础的本地 RAG 知识库问答流程。

通过该项目，可以理解 RAG 的核心思想：
不是让大模型凭空回答，而是先从知识库中找到相关内容，再让模型基于这些内容生成答案。

项目虽然简单，但涵盖了 RAG 应用开发中的关键环节，包括知识库处理、文本切分、内容检索、Prompt 构建、模型调用和历史记录保存。

后续可以继续接入向量数据库、Embedding 模型、Web 页面和真实大模型 API，将该 Demo 扩展成更完整的知识库问答系统。
#   a i - p r o m p t - r a g  
 