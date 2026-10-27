---
type: paper
status: 摘要核验
created: 2026-10-27
updated: 2026-10-27
tags:
  - s2st
---

# Direct Speech-to-Speech Translation With Discrete Units

## 题录与来源

- paper_id：`P06`；作者：Ann Lee, Peng-Jen Chen, Changhan Wang, Jiatao Gu, Sravya Popuri, Xutai Ma, Adam Polyak, Yossi Adi, Qing He, Yun Tang, Juan Pino, Wei-Ning Hsu。
- 年份/版本：2021 预印本；2022 正式发表；发表处：ACL 2022。
- 来源：[原始出版/报告页面](https://aclanthology.org/2022.acl-long.235/)；[arXiv:2107.05604](https://arxiv.org/abs/2107.05604)；[DOI:10.18653/v1/2022.acl-long.235](https://doi.org/10.18653/v1/2022.acl-long.235)。
- 本次核验日期：2026-10-27；范围/状态：题录、摘要、官方实现指南入口已核验；未完成复现。

## 研究任务与核心贡献

路线：直接式 / 离散单位。

任务和语言：Fisher 西班牙语→英语 S2ST；有/无文本监督设置。

核心贡献摘要：从目标语音抽取离散单位，训练语音到单位翻译；可联合输出语音与文字。 这是来源摘要层面的归纳，技术论证和消融证据仍需精读。

## 数据、评价与开放情况

- 数据集/训练与测试：Fisher Spanish-English；各设置的辅助任务和数据处理待核对。
- 评价指标：ASR 转写上的 BLEU；语音质量设置待正文确认。
- 代码/资料：[官方代码/资料入口](https://github.com/facebookresearch/fairseq/blob/main/examples/speech_to_speech/docs/direct_s2st_discrete_units.md)
- 权重：官方指南含预训练组件/模型入口；未逐个下载验证，部署语种需核对。
- 本地笔记：[模型持续笔记](../../03-模型研究/S2UT.md)。

## 证据提取区

| 待支持的具体判断 | 原文节/页/表 | 设置与比较条件 | 当前状态 |
| --- | --- | --- | --- |
| 核心方法为何有效 | 待填写 | 任务、数据、监督、模块与损失 | 待方法阅读 |
| 相对什么基线改善 | 待填写 | 方向、划分、预训练、评价器、方差 | 待逐表核对 |
| 作者明确局限 | 待定位；未提取不等于作者没有讨论 | 与本人的研究假设分开 | 待阅读 |

## 我的理解与问题

用自己的话写出一个模块的数据流，以及作者证据还不能支持的推广。待你阅读后填写；不要将上方资料摘要当作自己的理解。

返回[论文索引](../论文索引.md)；深入阅读使用[统一论文模板](../论文阅读模板.md)。
