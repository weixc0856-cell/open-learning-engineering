# 第二季：软件工程与系统边界 (Season 02)

> **06–10 · 如何把零散脚本组织成可靠的软件服务**  
> 主力对齐教材：[Cosmic Python (Architecture Patterns with Python)](https://www.cosmicpython.com/) · [MDN HTTP Guides](https://developer.mozilla.org/en-US/docs/Web/HTTP)

---

## 🎯 季度核心目标
当算法或计算脚本逐渐变大时，如果没有良好的架构分层，代码就会演变成无法维护的“面条代码”。
本季重点解决**系统边界与契约隔离**问题：学习如何通过领域模型（Domain Model）、服务层（Service Layer）与仓储模式（Repository Pattern），将核心业务逻辑与外界多变的数据库、UI 和外部 API 隔离开来。

---

## 📚 单元规划与核心机制

### [06] HTML、DOM 与结构化数据解析
- **核心概念**：标记语言语法树、DOM 节点层级、Web 组件化思维。
- **工程应用**：理解结构化标记如何表达层次关系，为后续的大模型结构化抽取奠定树形数据认知。

### [07] HTTP 协议、JSON 与 API 契约设计
- **核心概念**：HTTP/1.1 与 HTTP/2 协议帧；无状态性与会话保持；幂等性（GET/PUT vs POST）；语义化状态码（200/400/404/422/500）；JSON Schema 输入校验。
- **推荐阅读**：RFC 9110 HTTP Semantics, MDN HTTP 指南。

### [08] 缓存设计与边界代理
- **核心概念**：Cache-Control 标头；协商缓存（ETag, Last-Modified）；CDN 边缘节点原理；大文件分块流式传输。

### [09] 领域模型与核心业务规则 (Domain Model)
- **核心概念**：实体（Entity）与值对象（Value Object）的区别；领域不变量（Invariants）；通过强类型消除“基本类型偏执（Primitive Obsession）”。
- **实战配套**：[Lab 02: 领域建模与服务契约](../../../labs/02-architecture-service-contract/README.md)。

### [10] 模块边界、服务层与依赖注入 (Dependency Inversion)
- **核心概念**：仓储模式（Repository Pattern）解耦存储介质；服务层（Service Layer）编排应用用例；依赖反转（DIP）与 Mock 测试替身。
- **推荐阅读**：Cosmic Python 前言与第 1-4 章。
