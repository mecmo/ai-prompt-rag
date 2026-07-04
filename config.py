import os
from dotenv import load_dotenv

load_dotenv()

KNOWLEDGE_PATH = "docs/docker_knowledge.md"

SILICONFLOW_API_KEY = os.getenv("SILICONFLOW_API_KEY")
SILICONFLOW_BASE_URL = "https://api.siliconflow.cn/v1"

MODEL_NAME = "Qwen/Qwen3-8B"
TEMPERATURE = 0.2
TOP_K = 2

HISTORY_PATH = "result/history.md"