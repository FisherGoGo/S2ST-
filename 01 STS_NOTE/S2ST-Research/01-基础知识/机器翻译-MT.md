---
type: concept
status: 初稿
created: 2026-10-27
updated: 2026-10-27
tags:
  - s2st
---

# 机器翻译 MT：在文字层面保留意义

## 输入输出与系统位置

输入源语言文字，输出目标语言文字。中英词序、主语省略、数字表达都可能变化，不能按字替换。级联 S2ST 中的 MT 接收带识别错误和口语表达的文本，与干净书面翻译数据有分布差异。

典型神经 MT：文字→规范化→分词器→token IDs→编码器→目标解码器→反分词。例：“明天见”得到若干中文子词，目标序列不必有相同长度。分词器的 token 是整数符号，经 embedding 变为 `[B,T,D]`；目标 logits 是 `[B,Ty,V]`。

## 学习与推理

训练使用平行句对，通过交叉熵学习 $p(y\mid x)$。推理给定源 token 与目标语言条件，采用贪心或 beam search；过长输入需要明确分段，不能静默截断。[Transformer](Transformer与Seq2Seq.md)解释编码器和解码器。

[NLLB-200](../03-模型研究/NLLB-200.md)是可研究的多语翻译家族。实践可先考虑 distilled 600M，不能把该密集蒸馏模型说成原论文大型 MoE 的同一个架构。其分词配置中英语常用 `eng_Latn`，简体中文常用 `zho_Hans`；部署时再核对 tokenizer 和模型版本。语言代码也不同于 Whisper 的 `zh` 或 Seamless 的代码。

## 进入语音合成前检查什么

目标文字是 TTS 的内容约束，要保留原始译文和实际送入 TTS 的规范化文字，例如 “10:00” 被展开成怎样的读法。评价可用 BLEU、chrF、COMET，加双语人工检查，详见[语义与翻译质量](../05-质量评价/语义与翻译质量.md)。翻译分数衡量文字，不说明声音自然。

来源：[NLLB 论文](https://arxiv.org/abs/2207.04672)、[600M 官方模型卡](https://huggingface.co/facebook/nllb-200-distilled-600M)。学习问题：ASR 少了否定词时，MT 可能凭什么恢复它，又为什么不能依赖这种恢复？
