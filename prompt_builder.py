def build_prompt(query: str, contexts: list[str]) -> str:
    """
    根据用户问题和检索到的知识块，构造 RAG Prompt
    """
    knowledge = "\n\n---\n\n".join(contexts)

    prompt = f"""
请严格依据下面提供的知识回答问题。
如果知识中没有相关内容，请回答：知识库中未找到相关信息。
不要补充知识库中没有的信息。

【知识】
{knowledge}
【知识结束】

问题：
{query}
"""
    return prompt.strip()


if __name__ == "__main__":
    sample_query = "Docker Compose 是什么？"
    sample_contexts = [
        "Docker Compose 是 Docker 官方提供的多容器编排工具。"
    ]

    prompt = build_prompt(sample_query, sample_contexts)

    print(prompt)