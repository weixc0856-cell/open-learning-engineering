# Lab 06: 受控智能体状态机与契约闭环 (Controlled Agent Workflow)

## 📌 实验目标
大语言模型本质是概率生成器，容易产生语法合法但逻辑冲突的动作。
在严肃工程中，必须通过**确定性有限状态机（FSM）+ JSON Schema 强类型约束 + 审计日志**包裹 Agent。
本实验实现一个受控智能体工作流引擎：
1. **Schema 校验与反思修复**：拦截模型输出的非法字段或越界参数，触发修正重试。
2. **状态机跃迁守卫**：强制按照 `PENDING -> VALIDATING -> EXECUTING -> COMPLETED` 顺序执行。
3. **不可篡改审计追踪**：记录每一个操作时间戳、执行者与参数。

## 📜 运行测试
```bash
python3 -m unittest test_workflow.py -v
```
