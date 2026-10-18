# 贡献指南 (Contributing Guide)

感谢您关注并愿意参与建设 **理解技术 · 驾驭 AI (Understanding Technology, Working with AI)** 开源教育项目！

本项目致力于通过系统化的知识梳理、权威的原始证据索引和严谨的可复现实验，帮助跨学科学习者建立扎实的计算机与 AI 工程能力。为了确保整个知识体系的长久可信与工程交付质量，所有贡献均须遵循以下工作规范。

---

## 🧭 四步闭环研发工作流 (The 4-Stage Development Workflow)

任何新增或重大修改的课程单元均须依序通过以下四个阶段：

```text
[阶段 1: 资源审计] ➔ [阶段 2: 课程编写] ➔ [阶段 3: 工程实验] ➔ [阶段 4: 质量验收]
```

### 1. 资源审计 (Source Audit)
- 严禁根据二次营销文章、未经核实的博客或单纯的视频标题撰写课程。
- 必须找到并核查原作者、官方规范、学术论文或经确认的完整教材。
- 必须记录资料的获取渠道、全文可读性、具体版本号及版权许可（详见 `docs/references/source-index.md`）。

### 2. 课程编写 (Content Drafting)
- 每个单元建议固定包含以下结构：
  1. **本单元要解决的工程问题**（Context & Problem）
  2. **核心概念与机制解析**（Principles & Mechanics）
  3. **权威资料与深度建议**（Sources & Depth Guidance：明确区分必修、建议选修与原始精读）
  4. **动手实践与自检验证**（Hands-on Lab & Verification）
  5. **已知限制与失效边界**（Limitations & Boundaries）
- 严格区分“官方定义”、“推导证据”、“可复现实验”与“个人直觉类比”。严禁以比喻代替推导或测试。

### 3. 工程实验开发 (Engineering Labs)
- 实验必须具备明确的输入、输出规范与预期状态。
- 运行步骤必须完备且最小化，锁定依赖版本（如 `requirements.txt` 或标准库）。
- 必须包含自动化测试或确定性验证脚本（如 `test_*.py` 或 `test_*.sh`）。未经实际运行验证的代码不得标为“已通过”。

### 4. 质量验收与合并 (Quality Gate Acceptance)
- 遵循 `docs/quality-gates.md` 设定的四级验收网关标准。
- 本地运行自动化核验脚本：`python3 scripts/verify_repo.py`，确认无失效断链、测试 100% 通过。

---

## 🌿 分支与提交规范 (Git Flow & Commit Guidelines)

1. **分支命名**：
   - 特性/课程新增：`feature/s01-shell-lesson` 或 `feature/lab-02-domain`
   - 文档与证据纠错：`fix/source-link-update`
   - 基础设施改进：`chore/ci-pipeline`

2. **提交信息格式 (Conventional Commits)**：
   ```text
   <type>(<scope>): <subject>

   <body>
   ```
   - `type`: `feat`, `fix`, `docs`, `test`, `chore`, `refactor`
   - `scope`: `s01`, `s02`, `lab`, `docs`, `infra`
   - 示例：`feat(s06): add controlled agent workflow lab and unit tests`

---

## 📋 Pull Request 提交流程

1. Fork 本仓库并基于 `main` 分支拉取新分支。
2. 完成修改并确保所有本地测试通过。
3. 提交 PR 并完整填写 Pull Request 模板中的检查清单。
4. 维护者将依据四级证据规范与质量网关进行 Code/Content Review。
