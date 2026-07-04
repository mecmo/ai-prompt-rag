from loader import load_markdown
from splitter import split_markdown
from retriever import retrieve
from prompt_builder import build_prompt
from llm import ask_llm
from config import KNOWLEDGE_PATH, TOP_K
from history import save_history
from logger import info, success


def main():

    info("Loading knowledge...")
    text = load_markdown(KNOWLEDGE_PATH)
    success("Knowledge loaded.")
    info("Splitting document...")
    chunks = split_markdown(text)
    success(f"Split into {len(chunks)} chunks.")

    print("Local RAG Knowledge QA Demo")
    print("Type exit to quit")
    print("-" * 40)

    while True:
        query = input("\nQuestion: ")

        if query.lower() == "exit":
            print("Program exited.")
            break

        info("Retrieving knowledge...")
        results = retrieve(query, chunks, top_k=TOP_K)
        success(f"Retrieved {len(results)} chunks.")

        if not results:
            print("\nNo related information found in knowledge base.")
            continue

        contexts = [chunk for score, chunk in results]
        prompt = build_prompt(query, contexts)

        print("\nRetrieved Chunks:")
        print("-" * 40)

        for i, (score, chunk) in enumerate(results, 1):
            print(f"\n[Chunk {i} | Score: {score}]")
            print(chunk)

        #print("\nGenerated RAG Prompt:")
        #print("-" * 40)
        #print(prompt)

        print("\nCalling SiliconFlow API...")
        info("Calling SiliconFlow API...")
        answer = ask_llm(prompt)
        success("Answer generated.")

        print("\nAI Answer:")
        print("-" * 40)
        print(answer)

        save_history(query, answer)


if __name__ == "__main__":
    main()