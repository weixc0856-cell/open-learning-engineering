# 第四季：计算机体系结构与 GPU

> **第 16–20 单元｜理解硬件，才知道优化为什么有效**

本季的目标不是让每位学习者立刻成为 CUDA 程序员，而是建立一套能解释性能现象的模型：数据从哪里来、计算在哪里发生、并行开销是什么，以及加速比为何经常低于预期。

<div class="season-meta" markdown>
**建议投入：** 3–5 周　 ·　 **先修：** 基本 C/Python，理解数组和函数　 ·　 **最终产出：** 一份可复现的 CPU/GPU 性能对比报告
</div>

## 学完后，你应该能做什么？

- 解释缓存、局部性、内存带宽和计算吞吐量之间的关系。
- 区分并发与并行，使用阿姆达尔定律估算加速上限。
- 读懂 GPU 的线程层次和 SIMT 执行模型，并知道它不等于“每个线程独占一个核心”。
- 用 Roofline 思路初步判断算力受限还是带宽受限。
- 把数据传输、内核启动、同步和测量方法纳入端到端成本。

## 学习单元

<details open>
<summary><strong>16｜CPU、缓存与数据局部性</strong></summary>

CPU 访问不同层级存储的成本差异很大。缓存利用时间局部性（近期访问的数据可能再次被访问）和空间局部性（相邻地址可能很快被访问）。因此，算法的访存模式可能与算术操作数量同样重要。

**思考实验：** 对二维数组分别按行、按列遍历，比较运行时间。先确认语言、数组布局、数据规模和测量方式，再解释结果；不要把某一台机器的数字当作普遍常数。

</details>

<details>
<summary><strong>17｜并行、同步与阿姆达尔定律</strong></summary>

并行并非免费。任务拆分、调度、通信、锁竞争和串行部分都会限制收益。阿姆达尔定律给出理想化上限：若串行比例为 \(s\)，使用 \(N\) 个处理单元时，加速比上限为 \(1/(s+(1-s)/N)\)。它是分析模型，不是对真实硬件的完整预测。

**练习：** 假设程序有 20% 无法并行，计算 2、4、8、16 个处理单元时的理论上限，再列出真实系统中还会增加哪些成本。

</details>

<details>
<summary><strong>18｜GPU 执行模型与内存层次</strong></summary>

CUDA 常见的组织层次是 Grid、Block、Thread；硬件以 warp 为单位执行线程组。共享内存可以降低某些数据重复访问成本，但需要正确同步，且可能受到容量、占用率和访问冲突影响。全局内存容量较大，但延迟与带宽特征不同。

```cpp
__global__ void add(const float* a, const float* b, float* c, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) c[i] = a[i] + b[i];
}
```

这段代码展示索引和边界检查，不代表完整的高性能实现。实际应用还需处理内存分配、数据传输、错误检查、计时和资源释放。

</details>

<details>
<summary><strong>19｜Roofline：算力受限还是带宽受限？</strong></summary>

算术强度可粗略理解为每搬运一个字节执行多少浮点运算。Roofline 模型用峰值计算能力与内存带宽共同估计性能上限。低算术强度的任务往往更容易受内存带宽限制；高算术强度任务才更有机会逼近计算吞吐量上限。

**注意：** 实际性能还会受到访存合并、缓存命中、占用率、指令依赖、精度模式和软件实现等因素影响。模型用于定位问题，不是保证性能的公式。

</details>

<details>
<summary><strong>20｜GPU 加速的真实成本</strong></summary>

端到端时间至少可能包含：主机端准备、Host→Device 传输、内核启动、设备计算、同步、Device→Host 传输和结果校验。只测内核而忽略数据搬运，可能得出对实际应用没有意义的加速比。

**实验报告至少记录：** CPU/GPU 型号、驱动与工具链版本、输入规模、数据类型、是否计入传输、预热方式、重复次数、统计口径和正确性校验。

</details>

## 交互自测

<div class="knowledge-check" data-quiz>
  <p><strong>1. 一个任务只需处理几百个元素，GPU 不一定更快，最合理的原因是什么？</strong></p>
  <label><input type="radio" name="q1" value="a"> GPU 的计算能力一定更弱</label>
  <label><input type="radio" name="q1" value="b"> 启动、传输和同步等固定成本可能超过计算收益</label>
  <p class="quiz-feedback" data-feedback="q1" hidden>正确。比较时要测量端到端成本，而不只是设备上的计算时间。</p>
  <p><strong>2. Roofline 模型最适合用来做什么？</strong></p>
  <label><input type="radio" name="q2" value="a"> 精确预测任何程序的运行时间</label>
  <label><input type="radio" name="q2" value="b"> 估计性能上限并初步判断瓶颈类型</label>
  <p class="quiz-feedback" data-feedback="q2" hidden>正确。它是有用的性能分析模型，但不会取代实际测量。</p>
  <button type="button" class="quiz-submit">检查答案</button>
  <p class="quiz-result" aria-live="polite"></p>
</div>

## 参考资料

- [Berkeley CS61C](https://cs61c.org/)：计算机组成与底层执行。
- [CMU 15-418/15-618](https://www.cs.cmu.edu/afs/cs/academic/class/15418-s20/www/)：并行计算概念参考（课程年份与资料可能变化）。
- [NVIDIA CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/)：CUDA 编程模型的官方说明。
- [NVIDIA CUDA Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/)：性能测量与优化方法。
- [Roofline 原始论文](https://doi.org/10.1145/1498765.1498785)：模型背景与适用边界。

> **完成标准：** 不只给出“快了几倍”，还要说明测了什么、没测什么、结果能否复现，以及这个结论能否迁移到真实工作负载。
