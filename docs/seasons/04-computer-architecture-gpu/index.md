# 第四季：计算机体系结构与 GPU (Season 04)

> **16–20 · 为什么某些程序能够被加速，另一些不能？**  
> 主力对齐教材：[UC Berkeley CS61C (Fall 2025)](https://www-inst.eecs.berkeley.edu/~cs61c/fa25/) · [CMU 15-418/15-618](https://www.cs.cmu.edu/afs/cs/academic/class/15418-s25/www/) · [NVIDIA CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-programming-guide/)

---

## 🎯 季度核心目标
不要人云亦云地认为“只要用了 GPU 就能快 100 倍”。
本季从物理硬件层面解构计算性能：理解 CPU 缓存命中（Cache Lines）、分支预测、SIMD 指令集；深入 NVIDIA GPU 架构（SM, Warp, Shared Memory）；掌握著名的 Roofline 性能模型，定量分析一个算法是“算力受限（Compute Bound）”还是“访存受限（Memory Bound）”。
