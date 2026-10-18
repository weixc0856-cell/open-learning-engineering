# 全景路线图与能力进阶矩阵 (The 30-Unit Curriculum Roadmap)

本项目构建了一条严密的能力演进路线：从底层的操作系统与进程，到架构契约与数值计算，再到硬件体系、科学机器学习与受控智能体闭环。

```text
[计算环境] ──> [软件工程] ──> [科学计算] ──> [体系架构/GPU] ──> [深度学习/SciML] ──> [受控Agent]
 (S01: 01-05)   (S02: 06-10)   (S03: 11-15)    (S04: 16-20)       (S05: 21-25)      (S06: 26-30)
```

---

## 阶段矩阵总表 (30 教学单元明细)

| 期次 | 季 | 单元名称 | 核心知识机制 | 权威来源对齐 | 验收实验 | 成熟度 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **01** | S01 | Shell 与进程机制 | 工作目录、PATH、环境变量、子进程与退出状态码 | MIT Missing Semester 2026, Linux 手册 | 环境变量与退出码验证脚本 | Practice |
| **02** | S01 | I/O 重定向与管道 | stdin/stdout/stderr、文件描述符、管道缓冲与重定向 | Missing Semester, TLCL 第7版 | 管道流式日志过滤器 | Practice |
| **03** | S01 | 数据流与文本处理 | grep, awk, sed, jq, sort, uniq; 流式与全量载入区别 | TLCL, Missing Semester | 求解器日志指标提取工具 | Practice |
| **04** | S01 | SSH 与长程会话管理 | SSH 密钥、端口转发、Tmux 会话生命周期与断线持久化 | SSH RFC, OpenSSH 手册 | 后台长任务守护脚本 | Practice |
| **05** | S01 | Git 底层与配置追踪 | 工作区/暂存区/版本库、树对象/提交对象、差异对比与回滚 | Pro Git 简体中文版 (v2) | 仿真工程配置多分支变更管理 | Practice |
| **06** | S02 | HTML 与结构化数据 | 标记语言规范、DOM 树结构、序列化与边界解析 | MDN Web Docs | DOM 树遍历与结构化数据校验 | Practice |
| **07** | S02 | HTTP 协议与 API 契约 | 请求/响应报文、状态码、无状态性、JSON 契约与幂等性 | RFC 9110 (HTTP), MDN | curl 交互与契约模拟服务 | Practice |
| **08** | S02 | 缓存分发与边界代理 | CDN 边缘节点、Cache-Control、失效机制与分块传输 | MDN Caching, Nginx Docs | 大文件分发与缓存命中率测试 | Index |
| **09** | S02 | 领域建模与业务规则 | 实体、值对象、领域不变量、单位量纲强类型约束 | Cosmic Python, DDD 理论 | 工业仿真参数强校验模型 | Practice |
| **10** | S02 | 分层架构与依赖反转 | Repository 仓储模式、Service Layer 服务层、依赖注入 | Cosmic Python 源码仓库 | 依赖倒置微服务架构实现 | Practice |
| **11** | S03 | 函数设计与类型契约 | 纯函数、副作用控制、类型注解 (PEP 484)、数据类 | Python 官方语言参考 | 严格类型检查的数学函数库 | Practice |
| **12** | S03 | 异常防御与测试驱动 | 语法错误 vs 逻辑异常、pytest 断言、参数化测试 | pytest 官方文档 | 边界测试套件驱动的计算器 | Practice |
| **13** | S03 | 迭代器、生成器与内存 | 惰性求值、`yield` 机制、大规模数据集内存测量 | Python 官方进阶教程 | GB 级文件流式内存对比基准 | Practice |
| **14** | S03 | NumPy 数组与向量化 | ndarray 内存布局 (C/Fortran)、广播规则、SIMD 向量化 | Python Data Science Handbook | 向量化与循环加速比测量 (100x) | Practice |
| **15** | S03 | 性能剖析与瓶颈定位 | cProfile, timeit, 内存分析、算法渐近复杂度 | Python Profiling 手册 | 工业数据处理热点路径优化 | Practice |
| **16** | S04 | CPU 架构与缓存层次 | L1/L2/L3 Cache、时间/空间局部性、流水线与分支预测 | Berkeley CS61C (Fall 2025) | 连续 vs 不规则访问时间基准 | Practice |
| **17** | S04 | 并行计算与同步开销 | 多线程/多进程、阿姆达尔定律、竞态条件、锁开销 | CMU 15-418, CS61C | 多线程累加与锁竞争测量 | Practice |
| **18** | S04 | GPU 执行模型与内存 | Grid/Block/Thread/Warp、共享内存与全局内存、SIMT | NVIDIA CUDA C++ Programming Guide | 向量加法 CUDA 内核与 CPU 对比 | Practice |
| **19** | S04 | Roofline 模型与瓶颈 | 运算强度 (FLOPs/Byte)、算力上限与带宽上限分析 | Roofline 原始论文, CUDA Best Practices | 算力受限 vs 带宽受限内核分析 | Index |
| **20** | S04 | GPU 加速的真实成本 | Host-Device 数据传输开销、内核启动延迟与小规模陷阱 | NVIDIA CUDA Best Practices Guide | 端到端加速有效性与阈值测定 | Practice |
| **21** | S05 | 计算图与微型自动微分 | 标量计算图、链式法则反向传播、梯度检查 | Karpathy Micrograd, D2L (第2章) | 从零实现 Micrograd 引擎 | Practice |
| **22** | S05 | 神经网络训练与泛化 | 损失函数、SGD/Adam、过拟合、正则化、验证集分离 | 动手学深度学习 (D2L) | 拟合非线性函数的训练与泛化 | Practice |
| **23** | S05 | 空间卷积与特征提取 | 局部感受野、参数共享、池化与张量维度变换 | CS231n 讲义, D2L 卷积层 | 物理空间场特征提取网络 | Practice |
| **24** | S05 | PINN：物理方程约束 | PDE 残差损失、自动微分求导、边界约束与权重权衡 | Raissi 原始论文, DeepXDE 文档 | 1D 波动/热传导方程 PINN 解算 | Practice |
| **25** | S05 | 神经算子与代理解算 | 傅里叶神经算子 (FNO)、无限维空间映射、泛化边界 | Li et al. FNO 论文, NeuralOperator | 简化流场回归基准对比实验 | Index |
| **26** | S06 | LLM 工作机制与边界 | Tokenizer、自回归生成、上下文窗口、确定性 vs 随机 | Berkeley Agentic AI, HuggingFace | 模型幻觉与不确定性量化实验 | Practice |
| **27** | S06 | 结构化输出与 Schema | JSON Schema 规范、确定性类型校验、修复循环 | OpenAI / Anthropic 规范 | 结构化参数提取与校验器 | Practice |
| **28** | S06 | 检索增强生成 (RAG) | 分块策略、向量检索、重排序 (Rerank)、来源溯源 | LLM Cookbook, Datawhale | 带引用验证的离线 RAG 验证系统 | Practice |
| **29** | S06 | 工具调用与状态机工作流 | Tool-Calling 协议、有限状态机 (FSM)、超时与重试 | LangGraph, Hello-Agents | 具故障恢复的工具调用状态机 | Practice |
| **30** | S06 | 受控 Engineering Agent | 任务契约、人工审批确认（Human-in-the-loop）、日志闭环 | 工业真实案例, OSSU | 工业级 CFD 自动化辅助智能体 | Project |
