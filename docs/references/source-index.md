# 权威原始资料索引卡片 (Source Index Cards)

本项目坚持“严禁二手洗稿，必须追溯一手权威来源”。以下卡片记录了各季度核心教材的最新核验信息与审计状态。

---

## 📑 核心资料审计索引卡

### SRC-01: MIT The Missing Semester of Your CS Education (2026)
- **官方网址**：[https://missing.csail.mit.edu/2026/](https://missing.csail.mit.edu/2026/)
- **发布机构/作者**：MIT CSAIL (Anish Athalye, Jon Gjengset, Jose Javier Gonzalez Ortiz)
- **版本/发布时间**：2026 年最新修订版
- **全文可读性**：已确认。在线提供讲义全文、配套作业与实验命令。
- **版权许可证**：[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
- **对应季度与期次**：第一季 [01, 02, 03, 04, 05]
- **审计结论与深度建议**：优先作为第一季教学骨干。需补充工业级脚本错误防御（`set -euo pipefail`）和实际日志分析工程样例。

### SRC-02: Pro Git (2nd Edition)
- **官方网址**：[https://git-scm.com/book/zh/v2](https://git-scm.com/book/zh/v2)
- **发布机构/作者**：Scott Chacon & Ben Straub (官方维护简体中文翻译)
- **版本/发布时间**：第二版 (在线持续维护维护勘误)
- **全文可读性**：已确认。官方全书免费开放阅读，章节结构完整。
- **版权许可证**：[CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/)
- **对应季度与期次**：第一季 [05]
- **审计结论与深度建议**：第 1-3 章用于日常基础，第 10 章“Git 内部原理”用于深入理解底层 Blob/Tree/Commit 对象寻址机制。

### SRC-03: Cosmic Python (Architecture Patterns with Python)
- **官方网址**：[https://www.cosmicpython.com/](https://www.cosmicpython.com/)
- **官方仓库**：[https://github.com/cosmicpython/book](https://github.com/cosmicpython/book)
- **发布机构/作者**：Harry Percival & Bob Gregory (O'Reilly)
- **版本/发布时间**：在线持续更新版
- **全文可读性**：已确认。在线书提供完整章节、架构推导与测试代码。
- **版权许可证**：CC BY-NC-ND 4.0 (禁止改编，因此本课程仅做引用与独立案例推导，不搬运原文)
- **对应季度与期次**：第二季 [09, 10]
- **审计结论与深度建议**：极佳的 Python 领域驱动架构参考。本课程使用工程计算任务替代原书的电商库存案例，独立实现仓储与服务层。

### SRC-04: Python Data Science Handbook (2nd Edition)
- **官方网址**：[https://jakevdp.github.io/PythonDataScienceHandbook/](https://jakevdp.github.io/PythonDataScienceHandbook/)
- **发布机构/作者**：Jake VanderPlas
- **版本/发布时间**：第二版 (在线 Jupyter Notebooks)
- **全文可读性**：已确认。全书代码与讲义均以 Notebook 形式开源。
- **版权许可证**：CC BY-NC-ND (文字) / MIT (代码)
- **对应季度与期次**：第三季 [14, 15]
- **审计结论与深度建议**：深入讲解 NumPy 数组广播法则、跨步（Strides）与内存视图。实验中需在现代 Python 3.11+ 环境重新验证测试。

### SRC-05: UC Berkeley CS61C: Great Ideas in Computer Architecture
- **官方网址**：[https://www-inst.eecs.berkeley.edu/~cs61c/fa25/](https://www-inst.eecs.berkeley.edu/~cs61c/fa25/)
- **发布机构/作者**：UC Berkeley EECS Department
- **版本/发布时间**：Fall 2025
- **全文可读性**：部分确认。公开日程包含 RISC-V、流水线、缓存与并行计算讲义。
- **版权许可证**：高校教学公开资料（未开放商用再分发，仅做学术引用）
- **对应季度与期次**：第四季 [16, 17]
- **审计结论与深度建议**：用于建立精准的 CPU 存储层次模型，打破“CPU 快、GPU 慢”的片面认知。

### SRC-06: NVIDIA CUDA C++ Programming Guide
- **官方网址**：[https://docs.nvidia.com/cuda/cuda-programming-guide/](https://docs.nvidia.com/cuda/cuda-programming-guide/)
- **发布机构/作者**：NVIDIA Corporation
- **版本/发布时间**：CUDA 12.x / 13.0 官方最新指南
- **全文可读性**：已确认。提供权威的硬件与执行模型官方规范。
- **版权许可证**：NVIDIA 专有文档版权（免费在线阅读，严格保留引用声明）
- **对应季度与期次**：第四季 [18, 19, 20]
- **审计结论与深度建议**：硬件机制（Thread, Warp, SM, Shared Memory）的最终裁定标准。必须以官方规范为准，防止误用旧版本过时特性。

### SRC-07: 动手学深度学习 (Dive into Deep Learning - D2L)
- **官方网址**：[https://zh.d2l.ai/](https://zh.d2l.ai/)
- **发布机构/作者**：Aston Zhang, Zachary C. Lipton, Mu Li, Alexander J. Smola
- **版本/发布时间**：中文第二版 (持续维护)
- **全文可读性**：已确认。全书文字、公式、PyTorch 代码完全开放。
- **版权许可证**：[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) (文字) / Apache-2.0 (代码)
- **对应季度与期次**：第五季 [21, 22, 23]
- **审计结论与深度建议**：第五季最核心的深度学习教材底座。

### SRC-08: Hello-Agents (从零开始构建智能体)
- **官方网址**：[https://datawhalechina.github.io/hello-agents/](https://datawhalechina.github.io/hello-agents/)
- **官方仓库**：[https://github.com/datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents)
- **发布机构/作者**：Datawhale 开源社区
- **版本/发布时间**：v1.0.3+ (2026)
- **全文可读性**：已确认。包含 Agent 概念、工具调用、ReAct 循环、多智能体协作与评测。
- **版权许可证**：[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
- **对应季度与期次**：第六季 [26, 27, 29]
- **审计结论与深度建议**：中文领域极其优质的 Agent 开源教材。本课程在其基础上重点强化工业系统的异常处理、数据校验与安全控制边界。
