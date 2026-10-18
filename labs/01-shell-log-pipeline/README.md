# Lab 01: 求解器日志流式解析流水线 (Solver Log Pipeline)

## 📌 实验目标
在工业工程与科学计算中，物理求解器（如 OpenFOAM, ANSYS Fluent 等）在后台运行时会输出成千上万行文本日志。
如果编写脆弱的脚本，不仅占用巨量内存，还容易在日志中途截断时引发隐蔽错误。
本实验要求实现一个**高鲁棒性、具备流式处理能力并严格遵守退出状态码规范的 Shell 批处理工具**。

## 📜 运行与测试
```bash
# 1. 运行解析脚本处理示例日志
bash process_solver_log.sh sample_solver.log

# 2. 运行自动化测试验证边界情况
bash test_pipeline.sh
```
