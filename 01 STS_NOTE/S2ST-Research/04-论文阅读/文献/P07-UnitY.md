---
type: paper
status: 摘要核验
created: 2026-10-27
updated: 2026-10-27
tags:
  - s2st
---

# UnitY: Two-pass Direct Speech-to-speech Translation with Discrete Units

## 题录与来源

- paper_id：`P07`；作者：Hirofumi Inaguma, Sravya Popuri, Ilia Kulikov, Peng-Jen Chen, Changhan Wang, Yu-An Chung, Yun Tang, Ann Lee, Shinji Watanabe, Juan Pino。
- 年份/版本：2022 预印本；2023 正式发表；发表处：ACL 2023。
- 来源：[原始出版/报告页面](https://aclanthology.org/2023.acl-long.872/)；[arXiv:2212.08055](https://arxiv.org/abs/2212.08055)；[DOI:10.18653/v1/2023.acl-long.872](https://doi.org/10.18653/v1/2023.acl-long.872)。
- 本次核验日期：2026-10-27；范围/状态：题录与摘要已核验；官方代码根入口已知，专用配方/权重定位待核实。

## 研究任务与核心贡献

路线：两阶段直接式 / 文本与离散单位。

任务和语言：S2ST；各基准语言方向待正文逐表抄录，不能默认已验证中英双向。

核心贡献摘要：先生成语言表示再生成目标单位，结合第一阶段文本预训练与搜索设计。 这是来源摘要层面的归纳，技术论证和消融证据仍需精读。

## 数据、评价与开放情况

- 数据集/训练与测试：多种规模基准；具体数据/方向/划分待核对。
- 评价指标：ASR-BLEU、解码加速；计时范围和硬件待读取。
- 代码/资料：[官方代码/资料入口](https://github.com/facebookresearch/fairseq/tree/main/examples/speech_to_speech)
- 权重：本次未确认独立原版 UnitY checkpoint；Seamless 的 UnitY/UnitY2 不是原论文复现权重的同义词。
- 本地笔记：[模型持续笔记](../../03-模型研究/UnitY.md)。

## 证据提取区

| 待支持的具体判断 | 原文节/页/表 | 设置与比较条件 | 当前状态 |
| --- | --- | --- | --- |
| 核心方法为何有效 | 待填写 | 任务、数据、监督、模块与损失 | 待方法阅读 |
| 相对什么基线改善 | 待填写 | 方向、划分、预训练、评价器、方差 | 待逐表核对 |
| 作者明确局限 | 待定位；未提取不等于作者没有讨论 | 与本人的研究假设分开 | 待阅读 |

## 我的理解与问题

用自己的话写出一个模块的数据流，以及作者证据还不能支持的推广。待你阅读后填写；不要将上方资料摘要当作自己的理解。

返回[论文索引](../论文索引.md)；深入阅读使用[统一论文模板](../论文阅读模板.md)。
