# 理解技术 · 驾驭 AI (Understanding Technology, Working with AI)

> **从计算机基础到 AI 工程实践的开放式学习体系**  
> An open-source, evidence-based learning framework bridging computer fundamentals, software engineering, and AI systems.

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/Docs-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/weixc0856-cell/open-learning-engineering/actions/workflows/ci.yml/badge.svg)](https://github.com/weixc0856-cell/open-learning-engineering/actions/workflows/ci.yml)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 🎯 项目初衷与愿景 (Why This Project Exists)

生成式 AI（如 Claude, Codex, GPT 等）正在深刻重构软件开发与工程实践。今天，任何人都可以通过自然语言快速生成代码、文档、页面甚至完整应用。

**然而，“能够生成代码”不等于“理解代码”；“程序能够运行”不等于“系统正确、可靠、可维护”。**

当使用者缺乏基本的操作系统、网络、数据结构、架构契约与测试知识时，往往无法识别表面合理、实际潜藏严重缺陷的 AI 产出。批判性思维绝不能沦为空洞口号，它必须建立在**坚实的计算机基础、权威的原始证据与可复现的工程验证**之上。

**本项目不致力于成为追逐热点工具的提示词（Prompt）合集，也不做浮夸的几小时速成演示。** 我们的使命是：
1. **构建系统的工程认知地图**：降低跨学科、非科班学习者筛选与组织高质量技术资料的成本。
2. **连接专业教材与动手实践**：以权威公开课程（MIT Missing Semester, Cosmic Python, Berkeley CS61C, D2L, Hello-Agents 等）为基础，提供清晰的先修关系、深度建议与最小复现实验。
3. **践行受控的 Vibe Coding**：人负责需求分析、系统边界、接口契约与验收标准；AI 辅助实现；自动化测试与可执行代码提供客观验证证据。

---

## 👥 目标受众 (Target Audience)

- **跨行业工程与科研人员**：来自机械、车辆、CFD 仿真、材料、物理、化工等领域，希望借助 AI 构建专业自动化工具与数据系统的工程师。
- **技术转型与自学开发者**：希望建立系统计算机基础与现代软件工程素养的初学者。
- **AI 工具重度使用者**：已能熟练调用 LLM 工具，但希望深入理解系统底层原理、打破“黑盒依赖”并具备交付级验证能力的学习者。

---

## 🗺️ 全景课程路线图 (The 6-Seasons Roadmap)

项目设计为循序渐进的六大能力进阶阶段，涵盖从计算环境到受控智能体的完整链路：

```text
[第一季: 计算环境与工具] ➔ [第二季: 软件工程与边界] ➔ [第三季: Python 与科学计算]
                                                                  ↓
[第六季: 大模型工程与Agent] 🠔 [第五季: 深度学习与科学ML] 🠔 [第四季: 计算机体系结构与GPU]
```

| 季度 (Season) | 核心主题 (Topic) | 核心解决的问题 (Core Question) | 核心参考资料 (Primary Sources) | 阶段产出 (Deliverable) |
| :--- | :--- | :--- | :--- | :--- |
| **第一季 (S01)** | [计算环境与开发工具](docs/seasons/01-computer-foundations/index.md) | 工程师如何可靠地操作操作系统与版本？ | MIT Missing Semester, Pro Git, TLCL | 健壮的工程日志流式提取与批处理流水线 |
| **第二季 (S02)** | [软件工程与系统边界](docs/seasons/02-software-engineering/index.md) | 如何把零散脚本组织成健壮可靠的服务？ | Cosmic Python, MDN HTTP, Flask Architecture | 领域驱动分层架构与 API 契约微服务 |
| **第三季 (S03)** | [Python 与科学计算](docs/seasons/03-python-and-scientific-computing/index.md) | 如何编写高效、可测、向量化的计算程序？ | Python Data Science Handbook, NumPy, pytest | 向量化加速与内存剖析数值计算库 |
| **第四季 (S04)** | [计算机体系结构与 GPU](docs/seasons/04-computer-architecture-gpu/index.md) | 为什么某些程序能被加速，另一些不能？ | Berkeley CS61C, CMU 15-418, NVIDIA CUDA Guide | CPU 缓存层次与 GPU 并行加速对比基准 |
| **第五季 (S05)** | [深度学习与科学机器学习](docs/seasons/05-deep-learning-sciml/index.md) | 如何理解数学机制并应用于工程物理预测？ | 动手学深度学习 (D2L), Karpathy Micrograd, PINN | 微型自动微分引擎与科学机器学习预测基线 |
| **第六季 (S06)** | [大模型工程与受控自动化](docs/seasons/06-llm-and-agents/index.md) | 如何将随机的模型生成纳入确定性工程？ | Hello-Agents, LangGraph, JSON Schema, Berkeley | 具人机协同审批边界的自动化 Engineering Agent |

---

## ⚖️ 四级证据标准 (Four-Tier Evidence Framework)

为保证课程严谨度，所有技术结论均打上严格的证据级别标签：
- **一级（正式定义与标准规范）**：RFC 协议标准、官方 API 文档、经同行评议的严谨数学定义。
- **二级（教材推导与权威学术）**：经典教材推导、论文定理证明，明确保留前提假设与失效条件。
- **三级（可复现实验证据）**：本地可运行的代码、确定性测试用例、明确的软硬件环境与性能测量基准。
- **四级（教学类比与直觉解释）**：仅用于降低心智负担，不可作为技术正确性的独立依据。

---

## 📂 仓库目录结构 (Repository Layout)

```text
open-learning-engineering/
├── README.md                  # 项目总览与学习导航
├── CONTRIBUTING.md            # 贡献规范与 4 步工作流
├── CODE_OF_CONDUCT.md         # 社区行为准则
├── LICENSES.md                # 双许可协议完整说明
├── CITATION.cff               # 学术与项目引用元数据
├── mkdocs.yml                 # 在线文档站点构建配置
│
├── docs/                      # 核心教学内容与知识库 (Markdown)
│   ├── index.md               # 站点主页
│   ├── overview.md            # 项目初衷与详细纲领
│   ├── roadmap.md             # 30 期能力进阶矩阵与先修图谱
│   ├── principles.md          # 教学哲学与证据分级标准
│   ├── quality-gates.md       # 质量验收网关 (索引/实践/项目/发布级)
│   ├── licensing.md           # 知识产权与版权审计指南
│   ├── seasons/               # 六大季核心教学内容
│   │   ├── 01-computer-foundations/
│   │   ├── 02-software-engineering/
│   │   ├── 03-python-and-scientific-computing/
│   │   ├── 04-computer-architecture-gpu/
│   │   ├── 05-deep-learning-sciml/
│   │   └── 06-llm-and-agents/
│   └── references/            # 权威资料核验证据层
│       ├── source-index.md    # 核心学习资料检索卡片
│       └── license-audit.md   # 第三方许可证审计清单
│
├── labs/                      # 递进式可运行工程实验 (代码与测试)
│   ├── 01-shell-log-pipeline/ # S01: 日志解析与退出状态流
│   ├── 02-architecture-service-contract/ # S02: 领域模型与服务层解耦
│   └── 06-controlled-agent-workflow/     # S06: 受控智能体状态机闭环
│
├── projects/                  # 端到端交付级工程案例
│   └── engineering-agent/     # 工业仿真自动化智能体方案
│
├── scripts/                   # 自动化核验与构建工具脚本
│   ├── verify_repo.py         # 仓库完整性与实验测试验证器
│   └── check_sources.py       # 引用资料规范检查器
│
├── tests/                     # 仓库级结构化集成测试
│   └── test_structure.py
│
└── .github/                   # GitHub 协作规范与自动化 CI
    ├── workflows/ci.yml       # 自动化测试与站点校验
    ├── ISSUE_TEMPLATE/
    └── PULL_REQUEST_TEMPLATE.md
```

---

## 🧭 课程内容与交互方式

在线文档以“课程地图 → 分季导览 → 单元讲解 → 实验/自测”为主线。第三至第五季包含可展开的章节、代码片段与页面内自测；自测在浏览器本地执行，不会把答案发送到服务器。路线图列出的 30 个单元是规划范围，并不意味着每个单元都已达到完整讲义级别。欢迎通过 Issue 指出概念错误、缺失的练习或无法复现的步骤。

## 🚀 快速开始 (Getting Started)

### 1. 本地浏览文档 (MkDocs Material)
```bash
# 安装文档依赖 (可选)
pip install mkdocs-material

# 启动本地实时预览
mkdocs serve
# 访问 http://127.0.0.1:8000
```

### 2. 运行工程实验与自动化检验
```bash
# 运行仓库完整性验证器 (包含实验测试、链接合规与元数据检查)
python3 scripts/verify_repo.py

# 单独运行特定实验 (例如 S06: 受控 Agent 状态机实验)
python3 -m unittest discover -s labs/06-controlled-agent-workflow -p "test_*.py"
```

---

## 📜 许可证说明 (Dual-Licensing)

本项目采用**双重开源许可证**设计，以兼顾教育成果的公共属性与工程代码的自由流通：

- **课程讲义与文档 (`docs/`)**：基于 [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/) 许可发布。允许非商业性质的自由分享与改编，但须保留原作者署名并在相同协议下共享。
- **示例代码与实验脚本 (`labs/`, `projects/`, `scripts/`)**：基于宽松的 [MIT License](LICENSE) 许可发布，鼓励学习者与开发者无限制地用于学习、研究与商业衍生开发。
- **第三方引用内容**：严格遵循原作者许可证（详见 [docs/references/license-audit.md](docs/references/license-audit.md)）。

---

## 🤝 参与贡献 (Contributing)

我们热忱欢迎社区伙伴参与共建！在提交 Pull Request 前，请务必阅读：
- [CONTRIBUTING.md](CONTRIBUTING.md) — 了解基于证据的 4 步研发工作流
- [docs/quality-gates.md](docs/quality-gates.md) — 检查您的贡献是否符合当前网关标准

---

## 📮 引用本项目 (Citation)

如果您在学术研究、教程编写或开源工程中引用了本项目的内容，请参考 [CITATION.cff](CITATION.cff)：

```bibtex
@misc{wei2026openlearning,
  author = {Wayne Wei},
  title = {Understanding Technology, Working with AI: An Open Learning Engineering Framework},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/weixc0856-cell/open-learning-engineering}}
}
```
