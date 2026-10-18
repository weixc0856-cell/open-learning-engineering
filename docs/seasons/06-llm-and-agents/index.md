# 第六季：大模型工程与受控自动化 (Season 06)

> **26–30 · 从随机模型输出到确定性工程闭环**  
> 主力对齐教材：[Hello-Agents (Datawhale)](https://datawhalechina.github.io/hello-agents/) · [LangGraph Docs](https://docs.langchain.com/oss/python/langgraph/overview) · [UC Berkeley Agentic AI](https://rdi.berkeley.edu/agentic-ai/f25)

---

## 🎯 季度核心目标
在经历前五季计算机软硬件体系的洗礼后，本季进入现代 AI 最前沿的应用工程领域。
大语言模型本质是概率生成器，具有固有的“随机性”与“幻觉”倾向。在严肃的工程环境里，**绝不能把关键系统的控制权全权交托给黑盒模型**。
本季的核心使命是：**构建由确定性状态机包裹、严格依据 Schema 契约校验、拥有自动化重试与人工审批（Human-in-the-Loop）安全边界的受控工程智能体（Controlled Engineering Agent）**。

---

## 📚 单元规划与核心机制

### [26] 大模型工作机制与确定性边界
- **核心概念**：自回归生成、Next-Token 概率采样（Temperature / Top-P）；幻觉的根本成因；区分“语言流畅”、“逻辑自洽”与“事实正确”。
- **推荐阅读**：UC Berkeley Agentic AI 课程公开讲义。

### [27] 结构化输出契约与严格模式 (Structured Outputs)
- **核心概念**：JSON Schema 严格约束；Pydantic / Zod 数据验证；约束解码（Grammar-based Decoding）；校验失败时的自愈反思循环（Reflection Loop）。
- **实操要点**：任何 Agent 动作必须先映射为结构化强类型指令，严禁直接执行非结构化自然语言命令。

### [28] 知识检索与检索增强生成 (RAG) 评估
- **核心概念**：文档切分策略（Chunking Chunk-Size & Overlap）；向量检索与稀疏检索混合（Hybrid Search）；重排序（Reranking）；事实溯源与引用校验。
- **推荐阅读**：Datawhale 《面向开发者的 LLM 入门教程》。

### [29] 工具调用、状态机与容错恢复 (Tool Calling & FSM)
- **核心概念**：Tool Calling 协议；有限状态机（Finite State Machine）；幂等工具设计；超时控制、断网重试与补偿回滚机制。
- **实战配套**：[Lab 06: 受控 Agent 状态机工作流](../../../labs/06-controlled-agent-workflow/README.md)。

### [30] 综合工程案例：受控工程智能体闭环 (Capstone Project)
- **核心概念**：任务契约定义 ➔ 仿真模板渲染 ➔ 结构化参数校验 ➔ 模拟求解运行 ➔ 诊断日志分析 ➔ **人类审批门禁（Human Approval Gate）** ➔ 报告交付。
- **终极大作业**：[Projects: Engineering Agent](../../../projects/engineering-agent/README.md)。
