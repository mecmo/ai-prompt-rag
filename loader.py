from pathlib import Path


def load_markdown(file_path: str) -> str:
    """
    读取 Markdown 知识库
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"找不到文件：{file_path}")

    return path.read_text(encoding="utf-8")


if __name__ == "__main__":
    content = load_markdown("docs/docker_knowledge.md")

    print("=" * 50)
    print(content)