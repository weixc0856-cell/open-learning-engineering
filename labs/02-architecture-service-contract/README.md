# Lab 02: 领域建模与服务契约解耦 (Domain Modeling & Service Contract)

## 📌 实验目标
本实验践行第二季 **Cosmic Python** 的领域驱动设计思想。
构建一个工业计算任务的微型调度服务：
1. **值对象 (Value Object)**：`SimulationConfig` 封装不可变配置与强量纲校验。
2. **实体 (Entity)**：`SimulationTask` 封装计算生命周期（PENDING ➔ RUNNING ➔ COMPLETED/FAILED）与状态迁移守卫。
3. **仓储与服务层 (Repository & Service Layer)**：通过依赖反转将内存仓储与上层调度编排彻底解耦。

## 📜 运行测试
```bash
python3 -m unittest test_service.py -v
```
