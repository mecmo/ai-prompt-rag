import re


def split_markdown(text: str):
    """
    根据 Markdown 二级标题(##)切分知识块
    """
    pattern = r'(?=^##\s+)'

    chunks = re.split(pattern, text, flags=re.MULTILINE)

    chunks = [chunk.strip() for chunk in chunks if chunk.strip()]

    return chunks


if __name__ == "__main__":
    from loader import load_markdown

    text = load_markdown("docs/docker_knowledge.md")

    chunks = split_markdown(text)

    print(f"共切分出 {len(chunks)} 个 Chunk\n")

    for i, chunk in enumerate(chunks, 1):
        print("=" * 50)
        print(f"Chunk {i}")
        print("=" * 50)
        print(chunk)
        print()