---
type: paper
status: 摘要核验
created: 2026-10-27
updated: 2026-10-27
tags:
  - s2st
---

# Can We Achieve High-quality Direct Speech-to-Speech Translation without Parallel Speech Data?

## 题录与来源

- paper_id：`P10`；作者：Qingkai Fang, Shaolei Zhang, Zhengrui Ma, Min Zhang, Yang Feng。
- 年份/版本：2024；发表处：ACL 2024。
- 来源：[原始出版/报告页面](https://aclanthology.org/2024.acl-long.392/)；[arXiv:2406.07289](https://arxiv.org/abs/2406.07289)；[DOI:10.18653/v1/2024.acl-long.392](https://doi.org/10.18653/v1/2024.acl-long.392)。
- 本次核验日期：2026-10-27；范围/状态：题录摘要、正文 §3–4 的适配/对齐机制已定位核验；实验表格待精读。

## 研究任务与核心贡献

路线：组合式 / 两阶段直接式。

任务和语言：CVSS 上的 S2ST；ComSpeech-ZS 不使用平行 S2ST 语音，但仍使用 S2TT 与 TTS 配对数据。

核心贡献摘要：用词表适配器衔接 S2TT 与 TTS；用表示对齐学习复用非 S2ST 平行数据。 这是来源摘要层面的归纳，技术论证和消融证据仍需精读。

## 数据、评价与开放情况

- 数据集/训练与测试：CVSS，及 S2TT/TTS 数据；论文具体语种和数据规模见 §5.1 待提取。
- 评价指标：ASR-BLEU、解码速度、BLASER 2.0；分项结果待核对。
- 代码/资料：[官方代码/资料入口](https://github.com/ictnlp/ComSpeech)
- 权重：官方仓库提供训练/推理配方；本次未确认可直接下载的完整公开推理 checkpoint。
- 本地笔记：[模型持续笔记](../../03-模型研究/ComSpeech.md)。

## 证据提取区

| 待支持的具体判断 | 原文节/页/表 | 设置与比较条件 | 当前状态 |
| --- | --- | --- | --- |
| 核心方法为何有效 | 待填写 | 任务、数据、监督、模块与损失 | 待方法阅读 |
| 相对什么基线改善 | 待填写 | 方向、划分、预训练、评价器、方差 | 待逐表核对 |
| 作者明确局限 | 待定位；未提取不等于作者没有讨论 | 与本人的研究假设分开 | 待阅读 |

## 我的理解与问题

用自己的话写出一个模块的数据流，以及作者证据还不能支持的推广。待你阅读后填写；不要将上方资料摘要当作自己的理解。

返回[论文索引](../论文索引.md)；深入阅读使用[统一论文模板](../论文阅读模板.md)。
