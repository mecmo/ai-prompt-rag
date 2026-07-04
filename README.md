# AI Prompt RAG Practice

A local Retrieval-Augmented Generation (RAG) system built with Prompt Engineering and SiliconFlow LLM API.

---

## Overview

This project implements a full RAG pipeline for question answering over a local Markdown knowledge base.

It includes:

- Document loading
- Text chunking
- Keyword-based retrieval
- Prompt construction
- LLM inference (SiliconFlow Qwen3)
- Conversation history storage
- Logging system
- Config management

---

## Architecture

User Query  
→ Retriever  
→ Prompt Builder  
→ SiliconFlow LLM  
→ Answer

---

## Tech Stack

- Python 3.9+
- SiliconFlow API
- Qwen3
- Jieba
- Markdown Processing
- Custom RAG Pipeline

---

## Project Structure

AI-Prompt-RAG-Practice
│
├── app.py
├── config.py
├── llm.py
├── loader.py
├── splitter.py
├── retriever.py
├── prompt_builder.py
├── history.py
├── logger.py
│
├── docs/
│   └── docker_knowledge.md
│
├── result/
│   └── history.md
│
├── prompt/
├── logs/
└── README.md

---

## Features

Prompt Engineering:
- Role-based prompting
- Context injection
- Output constraints
- Few-shot examples
- RAG structured prompts

RAG Pipeline:
- Document loading
- Chunk splitting
- Keyword retrieval
- Prompt building
- LLM generation

LLM Integration:
- SiliconFlow API
- Qwen3 model
- Natural language QA

History:
- Automatic Q&A logging to result/history.md

Logging:
- INFO
- SUCCESS
- WARNING
- ERROR

---

## Usage

Install dependencies:
pip install -r requirements.txt

Create .env file:
SILICONFLOW_API_KEY=your_api_key

Run project:
python app.py

---

## Example

Question:
Docker Compose是什么？

Answer:
Docker Compose is a tool for defining and running multi-container applications.

---

## Highlights

- End-to-end RAG implementation
- Prompt engineering practice
- Real LLM API integration
- Modular Python architecture
- Resume-ready project
- Extensible design (FAISS / LangChain ready)

---

## Future Work

- Vector database (FAISS / Milvus)
- Embedding-based retrieval
- Streamlit web UI
- Docker deployment
- LangChain refactor

---

## Learning Outcomes

- Prompt engineering
- RAG system design
- LLM API integration
- Knowledge base QA system
- Python project architecture

---

## Target Roles

- AI Application Developer Intern
- Prompt Engineer Intern
- LLM Platform Engineer
- Cloud / AI Application Engineer

---

## License

MIT
