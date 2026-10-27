---
type: concept
status: 初稿
created: 2026-10-27
updated: 2026-10-27
tags:
  - s2st
---

# 语音识别 ASR：把声音转换成文字

## 解决的问题与接口

输入是一段带采样率的音频，输出是**源语言**文字，可附时间戳和置信信息。在级联系统里，它为 MT 提供内容；它自身不保证跨语言翻译。

常见流程：波形→重采样/特征→编码器→CTC 或序列解码器→文字。音频示意 `[B, N]`，特征 `[B, T, F]`，编码器 `[B, Tenc, D]`。[Whisper](../03-模型研究/Whisper.md)是适合第一轮推理实践的 Transformer Encoder–Decoder 实例。

## 两种训练思路

- **CTC**：输入帧多于文字，不知道每个字对应哪帧。CTC 对能折叠为正确文字的多条单调路径求和，使用 blank 符号。它不能简单当作逐帧真实标签训练。
- **Attention Encoder–Decoder**：根据输入表示和真实文字前缀预测下一 token，用交叉熵。推理再自回归生成，参见[Seq2Seq](Transformer与Seq2Seq.md)。现代 ASR 还有 Transducer，此处留作后续分支。

## 怎样判断识别是否出错

英文常报告 $WER=(S+D+I)/N$；中文通常先考虑 CER，必须说明是否保留标点、数字和大小写。错误率可超过 100%，因为插入数可能很多。低 WER 不等于翻译所需的关键信息完全正确：把“十点”认成“四点”可能比几个语气词更严重。

在[级联实验](../07-实验/实验路线与比较协议.md)中保存人工源转写和 ASR 输出；用人工源转写替换 ASR 是定位误差的工具。生成音频的“评价 ASR”与系统里的“源 ASR”承担不同角色。

来源入口：[Whisper 论文](https://proceedings.mlr.press/v202/radford23a.html)、[CTC 原论文](https://www.cs.toronto.edu/~graves/icml_2006.pdf)（CTC 推导待阅读）。
