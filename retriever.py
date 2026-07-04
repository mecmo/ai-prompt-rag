import jieba


def retrieve(query: str, chunks: list[str], top_k: int = 2) -> list[tuple[int, str]]:
    """
    根据用户问题，从 chunks 中检索最相关的知识块
    """
    query_words = set(jieba.lcut(query))

    scored_chunks = []

    for chunk in chunks:
        chunk_words = set(jieba.lcut(chunk))
        score = len(query_words & chunk_words)
        scored_chunks.append((score, chunk))

    scored_chunks.sort(key=lambda x: x[0], reverse=True)

    return [(score, chunk) for score, chunk in scored_chunks[:top_k] if score > 0]


if __name__ == "__main__":
    from loader import load_markdown
    from splitter import split_markdown

    text = load_markdown("docs/docker_knowledge.md")
    chunks = split_markdown(text)

    query = input("请输入问题：")

    results = retrieve(query, chunks)

    print("\n检索结果：")
    print("=" * 50)

    for i, (score, chunk) in enumerate(results, 1):
        print(f"\nChunk {i} | 匹配分数：{score}")
        print("-" * 50)
        print(chunk)