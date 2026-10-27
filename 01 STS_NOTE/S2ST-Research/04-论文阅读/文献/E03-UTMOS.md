---
type: paper
status: 摘要核验
created: 2026-10-27
updated: 2026-10-27
tags:
  - s2st
---

# UTMOS: UTokyo-SaruLab System for VoiceMOS Challenge 2022

## 题录与来源

- paper_id：`E03`；作者：Takaaki Saeki, Detai Xin, Wataru Nakata, Tomoki Koriyama, Shinnosuke Takamichi, Hiroshi Saruwatari。
- 年份/版本：2022；发表处：Interspeech 2022。
- 来源：[原始出版/报告页面](https://www.isca-archive.org/interspeech_2022/saeki22c_interspeech.html)；[DOI:10.21437/Interspeech.2022-439](https://doi.org/10.21437/Interspeech.2022-439)。
- 本次核验日期：2026-10-27；范围/状态：题录与摘要已核验；域外中英生成适用性待检验。

## 研究任务与核心贡献

路线：评价 / 语音主观分数预测。

任务和语言：VoiceMOS 的域内/域外 MOS 预测；不能视为中英翻译质量模型。

核心贡献摘要：结合 SSL 特征和强弱学习器预测主观分数。 这是来源摘要层面的归纳，技术论证和消融证据仍需精读。

## 数据、评价与开放情况

- 数据集/训练与测试：VoiceMOS 2022，来自 Blizzard/Voice Conversion Challenges 等。
- 评价指标：MOS 预测误差及相关性；分项排名和设置待表格核对。
- 代码/资料：[官方代码/资料入口](https://github.com/sarulab-speech/UTMOS22)
- 权重：官方实现入口；具体 predictor 版本待选择、权重未下载。
- 本地笔记：[综述写作框架](../../06-综述写作/综述提纲.md)。

## 证据提取区

| 待支持的具体判断 | 原文节/页/表 | 设置与比较条件 | 当前状态 |
| --- | --- | --- | --- |
| 核心方法为何有效 | 待填写 | 任务、数据、监督、模块与损失 | 待方法阅读 |
| 相对什么基线改善 | 待填写 | 方向、划分、预训练、评价器、方差 | 待逐表核对 |
| 作者明确局限 | 待定位；未提取不等于作者没有讨论 | 与本人的研究假设分开 | 待阅读 |

## 我的理解与问题

用自己的话写出一个模块的数据流，以及作者证据还不能支持的推广。待你阅读后填写；不要将上方资料摘要当作自己的理解。

返回[论文索引](../论文索引.md)；深入阅读使用[统一论文模板](../论文阅读模板.md)。
