from datetime import datetime
from config import HISTORY_PATH


def save_history(question: str, answer: str):
    """
    保存问答记录
    """

    with open(HISTORY_PATH, "a", encoding="utf-8") as f:

        f.write("\n---\n\n")

        f.write(f"## Time\n")
        f.write(f"{datetime.now()}\n\n")

        f.write("## Question\n")
        f.write(question + "\n\n")

        f.write("## Answer\n")
        f.write(answer + "\n")