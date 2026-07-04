# Prompt优化与RAG模拟实验总结

## 一、实验目的

本实验围绕 Prompt Engineering 与 RAG（Retrieval-Augmented Generation）展开，通过多轮 Prompt 优化及模拟 RAG 实验，分析不同 Prompt 技术对大语言模型输出质量的影响，并理解知识增强生成的基本原理。

---

## 二、实验过程

本实验共进行了五轮 Prompt 优化。

### V1

普通 Prompt。

目的：

观察模型默认输出。

---

### V2

增加：

- Role
- Constraint

目的：

提升回答专业性和结构化程度。

---

### V3

增加：

- Context

目的：

让 AI 根据用户背景生成更加具有针对性的内容。

---

### V4

增加：

- Few-shot

目的：

提高输出格式一致性。

---

### V5

模拟 RAG。

目的：

观察知识上下文对回答准确性的影响。

---

## 三、实验结果

随着 Prompt 信息不断增加，模型输出逐渐发生变化：

- 回答更加专业
- 输出更加稳定
- 内容更加结构化
- 针对性明显提高
- 幻觉现象减少

---

## 四、实验结论

Prompt Engineering 并不是简单"提问"，而是通过角色设定、背景信息、输出约束、示例引导等方式，引导模型生成更加符合需求的内容。

在模拟 RAG 实验中，通过人为提供知识上下文，可以显著提高回答的准确性和可控性。

说明：

外部知识能够有效降低模型幻觉，提高回答稳定性。

---

## 五、项目收获

通过本项目，我掌握了：

- Prompt Engineering 基础方法
- Role Prompt
- Context Prompt
- Constraint Prompt
- Few-shot Prompt
- 模拟 RAG 工作流程
- 知识结构化方法
- Chunk 基本设计思路

同时，对 AI 应用开发中的知识库构建流程有了初步理解。