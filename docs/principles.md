# 教学哲学与证据分级标准 (Principles & Evidence Framework)

为确保知识体系的高质量沉淀，杜绝模糊推论与营销夸大，本项目设立严苛的技术结论证据分级制度与工程实践规范。

---

## 一、四级技术证据标准 (The Four-Tier Evidence Standard)

本体系中的所有核心章节、讲义和实验报告，均须遵循以下证据层级标注：

```text
一级证据: 正式定义与官方规范 (Standards & Specifications)
   │
二级证据: 权威教材推导与学术论证 (Textbooks & Peer-Reviewed Theory)
   │
三级证据: 可复现实验与自动化测试 (Reproducible Experiments & Benchmarks)
   │
四级证据: 教学类比与通俗直觉 (Pedagogical Analogies & Intuitions)
```

### 1. 一级证据：正式定义与规范 (Tier 1: Standards)
- **定义**：IETF RFC 标准、W3C 规范、ISO/IEC 标准、编程语言官方语言参考（Language Reference）以及框架官方 API 规范。
- **效力**：用于确立术语定义、协议格式、调用契约、错误码定义等最高准则。

### 2. 二级证据：权威教材推导与学术论证 (Tier 2: Academic Theory)
- **定义**：同行评议学术论文、经典大学教材（如 MIT, Berkeley, CMU 教学用书）中的严格数学证明与系统定理。
- **效力**：用于阐明算法复杂度、数学前提假设、系统性能理论上限（如 Roofline 模型、Amdahl 定律）。必须保留前提假设，不可断章取义。

### 3. 三级证据：可复现实验与基准测试 (Tier 3: Experiments)
- **定义**：本地或 CI 环境中可独立运行的代码、单元测试覆盖率、基准性能测量（包含硬件配置、编译器版本、输入数据集与误差棒）。
- **效力**：用于验证实际工程行为、内存占用、加速比与收敛曲线。任何声称“加速了 X 倍”或“解决了某问题”的结论，必须提供可复现的三级证据支持。

### 4. 四级证据：教学类比与个人直觉 (Tier 4: Pedagogical Analogies)
- **定义**：为了降低零基础学习者的心智认知成本而设计的通俗比喻与直觉图解。
- **效力**：仅作为启发思考与建立心智模型的辅助工具，严禁将四级证据作为技术正确性的独立论据。

---

## 二、受控的 Vibe Coding 原则 (Controlled Vibe Coding)

在生成式 AI 时代，我们不鼓励学习者退回手写每一个字符的低效状态，但坚决反对毫无控制的盲信：

1. **人类把控关键契约**：
   - 需求与业务边界（Domain Boundaries）
   - 数据模型与不变量（Entities & Invariants）
   - 接口输入输出规范（API Schemas & Contracts）
   - 异常处理策略与验收标准（Acceptance Tests）
2. **AI 辅助实现细节**：
   - 生成样板代码、数据转换函数、SQL 查询与前端组件。
   - 编写初始单元测试用例与 mock 数据。
3. **机器提供客观证据**：
   - 静态类型检查器（mypy / TypeScript）
   - 自动化测试套件（pytest / unittest）
   - 运行时日志与性能分析器（cProfile / perf）

只有通过机器检验的代码，才允许进入代码仓库；只有被测试覆盖的行为，才能被视为已被掌握。
