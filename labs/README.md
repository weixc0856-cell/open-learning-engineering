# 动手工程实验库 (Engineering Hands-on Labs)

本目录包含与课程体系紧密绑定的可独立运行的工程实验代码。

---

## 🎯 实验设计哲学 (Lab Philosophy)

> **“未经实际运行测试的代码，不得标记为已掌握；缺乏边界防御的脚本，不得投入生产。”**

每个实验均设计为一个自包含的微型工程模块，遵循以下硬性规范：
1. **最小依赖**：优先使用标准库（POSIX Shell、Python 3 标准库），免除复杂的环境安装负担。
2. **确定性测试**：每个实验均提供自动化测试脚本（`test_*.sh` 或 `test_*.py`），具备非零退出码保障。
3. **真实工业切片**：摒弃“Todo List”或玩具代码，均抽象自真实的工程计算、数据处理与智能体编排场景。

---

## 🧪 现有实验索引

| 实验编号 | 对应季度 | 实验名称 | 核心技术点 | 运行命令 |
| :--- | :--- | :--- | :--- | :--- |
| **Lab 01** | S01 | [求解器日志流式解析流水线](01-shell-log-pipeline/README.md) | POSIX Shell, 退出码, awk/grep, 流式 I/O | `bash labs/01-shell-log-pipeline/test_pipeline.sh` |
| **Lab 02** | S02 | [领域建模与服务契约解耦](02-architecture-service-contract/README.md) | 值对象, 仓储模式, 服务层, 单元测试 | `python3 -m unittest discover -s labs/02-architecture-service-contract` |
| **Lab 06** | S06 | [受控智能体状态机与契约闭环](06-controlled-agent-workflow/README.md) | JSON Schema, 有限状态机, 容错自愈, 审计日志 | `python3 -m unittest discover -s labs/06-controlled-agent-workflow` |
