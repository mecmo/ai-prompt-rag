from openai import OpenAI
from config import SILICONFLOW_API_KEY, SILICONFLOW_BASE_URL, MODEL_NAME, TEMPERATURE

client = OpenAI(
    api_key=SILICONFLOW_API_KEY,
    base_url=SILICONFLOW_BASE_URL
)


def ask_llm(prompt: str) -> str:
    if not SILICONFLOW_API_KEY:
        return "调用失败：未读取到 SILICONFLOW_API_KEY，请检查 .env 文件。"

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=TEMPERATURE
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"调用 LLM 失败：{e}"