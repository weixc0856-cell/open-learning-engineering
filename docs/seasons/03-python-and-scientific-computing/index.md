# 第三季：Python 与科学计算

> **第 11–15 单元｜从“脚本能跑”到“结果可信、性能可解释”**

本季不是 Python 语法大全，而是围绕工程计算最常见的五个问题组织：函数如何约定输入输出、错误如何被发现、数据如何流动、数组为什么快、优化应该从哪里开始。

<div class="season-meta" markdown>
**建议投入：** 2–4 周　 ·　 **先修：** 基本 Shell/Git，能读写简单 Python 脚本　 ·　 **最终产出：** 一个有类型约束、测试、基准测量的数值计算小库
</div>

## 学完后，你应该能做什么？

- 把单位、范围和异常条件写进接口，而不是依赖调用者“记得注意”。
- 用测试描述正常输入、边界输入和失败行为，并能解释测试覆盖不到什么。
- 处理大型日志或数据文件时，判断应一次性读入还是采用迭代器/生成器。
- 理解 NumPy 的数组形状、dtype、广播和内存布局，避免把 Python 循环误当成唯一方案。
- 用测量定位瓶颈，不把“改写后看起来更复杂”误当成优化。

## 学习单元

<details open>
<summary><strong>11｜函数设计、类型与数据契约</strong> <span class="tag">基础</span></summary>

**要回答的问题：** 一个函数到底承诺了什么？

函数不只是几行代码，它也是一个小型接口。调用者需要知道输入的含义、单位、允许范围、返回值和失败方式。

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class DragResult:
    cd: float
    reference_area_m2: float

def drag_coefficient(force_n: float, dynamic_pressure_pa: float,
                     reference_area_m2: float) -> DragResult:
    if dynamic_pressure_pa <= 0 or reference_area_m2 <= 0:
        raise ValueError("pressure and reference area must be positive")
    cd = force_n / (dynamic_pressure_pa * reference_area_m2)
    return DragResult(cd=cd, reference_area_m2=reference_area_m2)
```

**注意：** 类型注解主要帮助工具和读者理解接口；Python 默认不会自动执行完整的静态类型检查。单位也不会因为变量名写了 `_m2` 就自动正确，必要时仍要做显式校验。

**练习：** 为函数增加“阻力必须非负”的业务约束，并讨论这是否适用于所有坐标系和符号约定。

</details>

<details>
<summary><strong>12｜异常处理与测试驱动</strong> <span class="tag">基础</span></summary>

把错误分成三类：输入不合法、运行环境失败、程序自身缺陷。不要用一个宽泛的 `except Exception` 把三者全部吞掉。

```python
import pytest

@pytest.mark.parametrize("q, area", [(0.0, 2.0), (100.0, 0.0), (-1.0, 2.0)])
def test_invalid_denominator_is_rejected(q, area):
    with pytest.raises(ValueError):
        drag_coefficient(100.0, q, area)
```

**检查清单：** 正常路径、边界值、错误类型、错误信息、重复运行是否稳定。测试通过只能说明“这些断言在这些条件下成立”，不能证明程序没有任何缺陷。

**练习：** 给一个解析器编写至少 3 个失败测试，再修改实现让测试通过。

</details>

<details>
<summary><strong>13｜迭代器、生成器与内存</strong> <span class="tag">基础 → 实践</span></summary>

列表通常保存全部元素；生成器可以逐项产出数据。对于数 GB 的求解器日志，流式处理能避免把全部文本同时放进内存，但并不保证整个程序永远是常数内存——下游若不断累积结果，内存仍会增长。

```python
def read_residuals(path):
    with open(path, encoding="utf-8") as stream:
        for line in stream:
            if "Residual" in line:
                yield line.rstrip()

for row in read_residuals("solver.log"):
    print(row)
```

**练习：** 比较 `read()` 后整体筛选与逐行筛选。记录输入文件大小、峰值内存、运行时间和 Python 版本；不要只凭主观感受判断。

</details>

<details>
<summary><strong>14｜NumPy 数组、形状与向量化</strong> <span class="tag">核心</span></summary>

NumPy 的优势不仅是“少写循环”，还在于把大量同类数值操作交给底层编译实现。但向量化会带来临时数组、内存带宽和数据布局等成本。

```python
import numpy as np

velocity = np.array([20.0, 25.0, 30.0])  # m/s
rho = 1.225                              # kg/m^3
q = 0.5 * rho * velocity**2             # Pa，广播标量 rho
print(q)
```

重点掌握：`shape`、`dtype`、切片是否产生视图、广播规则、C/Fortran 连续布局，以及浮点误差。数组维度匹配不代表物理含义匹配，单位与坐标约定必须单独检查。

**练习：** 对相同输入分别使用 Python 循环和 NumPy 表达式，测量多个数据规模下的耗时；解释为什么小数组不一定更快。

</details>

<details>
<summary><strong>15｜性能剖析：先测量，再优化</strong> <span class="tag">实践</span></summary>

建议顺序：先定义正确性基线，再测端到端时间；之后用 `cProfile` 找热点、用 `timeit` 比较小片段，最后复测并检查结果是否变化。

- **不要**在没有基准的情况下声称“快了 100 倍”。
- **不要**把一次运行结果当作结论；考虑预热、输入规模、缓存和系统负载。
- **不要**为了微优化牺牲可读性，除非测量显示它确实影响目标工作负载。

**最终小项目：** 实现一个 CSV/日志数值汇总工具，要求输入校验、至少 8 个测试、流式读取选项、性能基准说明和已知限制。

</details>

## 自测：先判断，再展开答案

<div class="knowledge-check" data-quiz>
  <p><strong>1. 给函数加上 <code>value: float</code> 注解后，Python 默认会在运行时拒绝字符串吗？</strong></p>
  <label><input type="radio" name="q1" value="a"> 会，注解会自动验证类型</label>
  <label><input type="radio" name="q1" value="b"> 不会，通常需要静态检查工具或显式运行时校验</label>
  <p class="quiz-feedback" data-feedback="q1" hidden>正确。类型注解本身不是自动运行的输入验证器。</p>
  <p><strong>2. 使用生成器读取大文件，就能保证程序内存占用恒定吗？</strong></p>
  <label><input type="radio" name="q2" value="a"> 能，只要使用了 yield</label>
  <label><input type="radio" name="q2" value="b"> 不能，还要看下游是否持续累积数据</label>
  <p class="quiz-feedback" data-feedback="q2" hidden>正确。生成器降低了逐步读取的成本，但不能约束整个数据流水线的内存行为。</p>
  <button type="button" class="quiz-submit">检查答案</button>
  <p class="quiz-result" aria-live="polite"></p>
</div>

## 配套实验与参考资料

- 实验入口：[Labs 总览](../../../labs/README.md)。
- [Python 官方教程](https://docs.python.org/3/tutorial/)：语言行为的首要参考。
- [NumPy 用户指南](https://numpy.org/doc/stable/user/)：数组、广播与性能相关说明。
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)：数据分析实践参考。
- [pytest 文档](https://docs.pytest.org/)：测试组织与参数化测试。

> **完成标准：** 你能解释代码为什么正确、测试覆盖了什么、性能结论在什么条件下成立，以及哪些问题仍未验证。
