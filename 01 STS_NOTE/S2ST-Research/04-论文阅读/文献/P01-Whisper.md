---
type: paper
status: 摘要核验
created: 2026-10-27
updated: 2026-10-27
tags:
  - s2st
---

# Robust Speech Recognition via Large-Scale Weak Supervision

## 题录与来源

- paper_id：`P01`；作者：Alec Radford, Jong Wook Kim, Tao Xu, Greg Brockman, Christine McLeavey, Ilya Sutskever。
- 年份/版本：2022 预印本；2023 正式发表；发表处：ICML 2023，PMLR 202。
- 来源：[原始出版/报告页面](https://proceedings.mlr.press/v202/radford23a.html)；[arXiv:2212.04356](https://arxiv.org/abs/2212.04356)。
- 本次核验日期：2026-10-27；范围/状态：题录、摘要、官方 README 已核验；方法和实验待精读。

## 研究任务与核心贡献

路线：基础 ASR / S2TT。

任务和语言：多语言识别；非英语语音→英语文字翻译。中英实验优先使用识别模式。

核心贡献摘要：大规模弱监督多任务训练与跨数据集零样本泛化。 这是来源摘要层面的归纳，技术论证和消融证据仍需精读。

## 数据、评价与开放情况

- 数据集/训练与测试：680,000 小时多语训练音频；各测试集及语言分解待逐表读取。
- 评价指标：WER/CER；翻译 BLEU。
- 代码/资料：[官方代码/资料入口](https://github.com/openai/whisper)
- 权重：官方仓库的 Available models and languages / load_model 下载入口；权重未下载。
- 本地笔记：[模型持续笔记](../../03-模型研究/Whisper.md)。

## 证据提取区

| 待支持的具体判断 | 原文节/页/表 | 设置与比较条件 | 当前状态 |
| --- | --- | --- | --- |
| 核心方法为何有效 | 待填写 | 任务、数据、监督、模块与损失 | 待方法阅读 |
| 相对什么基线改善 | 待填写 | 方向、划分、预训练、评价器、方差 | 待逐表核对 |
| 作者明确局限 | 待定位；未提取不等于作者没有讨论 | 与本人的研究假设分开 | 待阅读 |

## 我的理解与问题

用自己的话写出一个模块的数据流，以及作者证据还不能支持的推广。待你阅读后填写；不要将上方资料摘要当作自己的理解。

返回[论文索引](../论文索引.md)；深入阅读使用[统一论文模板](../论文阅读模板.md)。
