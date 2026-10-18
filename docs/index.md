# 理解技术 · 驾驭 AI (Understanding Technology, Working with AI)

欢迎来到 **理解技术 · 驾驭 AI**（Open Learning Engineering）开源教育体系。

这是一个专为**跨学科学习者、工程科研人员与非科班自学者**打造的计算机与人工智能工程学习框架。

---

## 💡 核心信念 (Core Tenets)

> **“能够生成代码，不等于理解代码；能够运行程序，不等于系统可靠、可交付。”**

当前，大语言模型（LLM）使编写代码的门槛急剧降低。然而，这也带来了一个全新的工程挑战：
**当 AI 能够为你生成表面上极其专业的代码与架构时，如果你缺乏基本的计算机系统基础与软件工程素养，你凭什么判断它做得对不对？**

本项目坚持：
1. **批判性思维不能停留在口号**：真正的怀疑精神必须建立在扎实的计算机体系结构、操作系统、网络协议与软件契约知识之上。
2. **专业教材负责深度，课程体系负责组织与应用**：我们不重新发明轮子，而是精选世界一流大学与开源社区的权威公开资料（MIT, Berkeley, Harvard, D2L, Datawhale 等），梳理先修链路与阅读范围。
3. **受控的 Vibe Coding**：人类工程师负责明确需求、系统边界、接口契约与验收标准；AI 承担高效实现；确定性测试与自动化验证提供交付证据。

---

## 🧭 从哪里开始

<div class="learning-path" markdown>
<div>
**01 · 计算环境与工具**

命令行、进程、数据流、Git

[进入第一季 →](seasons/01-computer-foundations/index.md)
</div>
<div>
**02 · 软件工程与边界**

HTTP、接口契约、领域模型、分层

[进入第二季 →](seasons/02-software-engineering/index.md)
</div>
<div>
**03 · Python 与科学计算**

测试、内存、NumPy、性能分析

[进入第三季 →](seasons/03-python-and-scientific-computing/index.md)
</div>
<div>
**04 · 体系结构与 GPU**

缓存、并行、CUDA、Roofline

[进入第四季 →](seasons/04-computer-architecture-gpu/index.md)
</div>
<div>
**05 · 深度学习与 SciML**

自动微分、泛化、PINN、神经算子

[进入第五季 →](seasons/05-deep-learning-sciml/index.md)
</div>
<div>
**06 · 大模型与受控 Agent**

Schema、RAG、状态机、人工审批

[进入第六季 →](seasons/06-llm-and-agents/index.md)
</div>
</div>

建议先按顺序学习，但不必把所有内容一次学完。每个单元都应经历“提出问题 → 阅读原始资料 → 做最小实验 → 检查结果 → 记录限制”，而不是只看完讲解就算掌握。

- **[项目初衷与愿景 (Overview)](overview.md)**：深入理解本课程为什么存在、反对什么、提倡什么。
- **[教学哲学与证据分级 (Principles)](principles.md)**：了解四级证据体系与受控 Vibe Coding 规范。
- **[全景路线图 (Roadmap)](roadmap.md)**：30 个细分期次与知识单元的能力进阶矩阵。
- **[质量验收网关 (Quality Gates)](quality-gates.md)**：了解课程单元从“草稿”到“发布”的严谨准入要求。
- **[权威原始资料索引 (Source Index)](references/source-index.md)**：查看所有入选核心教材的审计状态与官方入口。
- **[动手工程实验 (Labs)](https://github.com/weixc0856-cell/open-learning-engineering/tree/main/labs)**：查看与运行各季度配套的自动化测试工程代码。

---

## 📌 如何使用本指南

- **如果你刚开始接触编程**：请从 [第一季：计算环境与开发工具](seasons/01-computer-foundations/index.md) 开始，在真实的命令行环境中亲手配置工作流。
- **如果你已有脚本编写经验，但系统总是脆弱**：请重点研读 [第二季：软件工程与系统边界](seasons/02-software-engineering/index.md) 与 [第三季：Python 与科学计算](seasons/03-python-and-scientific-computing/index.md)。
- **如果你希望借助 AI 构建复杂的自主智能体系统**：请深入学习 [第六季：大模型工程与受控自动化](seasons/06-llm-and-agents/index.md)，掌握结构化输出契约、状态机与异常恢复。


## 🧪 推荐学习节奏

1. **先读问题与目标**：明确本节要解释的现象，不急着记术语。
2. **打开折叠章节**：每个主题先看机制，再完成练习；不懂的地方回到原始资料。
3. **亲手运行实验**：记录环境、输入、预期结果和实际结果。
4. **做页面自测**：自测是检验理解的提示，不是能力认证。
5. **写下一个反例**：说明方法在哪些条件下会失效，或当前证据还不能支持什么结论。

> **内容成熟度说明：** 六季目录与 30 个单元路线图是整体规划；各单元的内容深度并不完全相同。当前第三至第五季已补充机制解释、练习和自测；第一、第二、第六季仍以单元导览为主，后续会逐步补齐独立讲义、可运行实验和验收标准。请以每节实际内容和实验状态为准，不把路线图误读为 30 篇完整讲义已经全部交付。
