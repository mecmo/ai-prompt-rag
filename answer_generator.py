def generate_answer(query: str, contexts: list[str]) -> str:
    """
    基于检索到的知识块生成简单回答
    当前版本不调用大模型，只从知识库中提取相关内容。
    """
    if not contexts:
        return "知识库中未找到相关信息。"

    knowledge = "\n\n".join(contexts)

    answer = f"""
根据知识库内容，回答如下：

{knowledge}
"""
    return answer.strip()