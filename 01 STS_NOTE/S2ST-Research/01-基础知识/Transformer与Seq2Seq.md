---
type: concept
status: 初稿
created: 2026-10-27
updated: 2026-10-27
tags:
  - s2st
---

# Transformer 与 Seq2Seq：CNN 之后需要补什么

## 先理解序列任务

CNN 识图常把固定大小图像映射为类别。Seq2Seq 则把长度为 $T_x$ 的输入映射为长度不同的 $T_y$ 输出，例如中文音频→英文 token。编码器产生上下文表示 $H$；解码器根据 $H$ 和已有目标前缀预测下一个符号。

| 张量 | 示意形状 | 含义 |
| --- | --- | --- |
| 输入特征 | `[B, Tx, F]` | 一批语音帧，每帧 F 个特征 |
| 编码器状态 | `[B, Tenc, D]` | 下采样后每个位置 D 维的表示 |
| 文本 token IDs | `[B, Ty]` | 整数索引，经 embedding 变为向量 |
| 解码器 logits | `[B, Ty, V]` | 每个位置对 V 个词表符号的未归一化分数 |

这是教学约定，PyTorch/不同模型可能交换轴。Mask 遮住 padding，因果 mask 阻止解码器看到未来答案。

## Attention 在做什么

$\operatorname{Attention}(Q,K,V)=\operatorname{softmax}(QK^\top/\sqrt{d_k})V$。

Q 是当前位置提出的查询，K 是候选位置的匹配特征，V 是要汇总的信息。Self-attention 在同一序列内找关系，Cross-attention 让目标位置查询源序列。多头关注不同子空间；位置编码提供顺序；前馈网络变换每个位置；残差连接和归一化帮助深层训练。注意力权重可用于观察，但不能直接当作完整因果解释。

## 训练与推理必须分开画

自回归训练常用真实前缀（teacher forcing）计算所有目标位置：

$$\mathcal L_{CE}=-\sum_t\log p(y_t\mid y_{<t},H).$$

交叉熵要求正确 token 概率变高；padding 位置不计入损失。推理时先给开始符号，再把模型自己的输出接回输入，直到结束符号或长度上限；贪心选最大概率，beam search 保留多个候选，采样按分布抽取。训练能并行计算位置，不意味着 AR 推理也能一次生成整句。

NAR 模型让某些输出位置并行预测，往往需要长度/时长预测和对齐机制；它仍可能处在包含 AR 翻译解码器的系统里。[SeamlessM4T v2](../03-模型研究/SeamlessM4T-v2.md)是一个区分模块的练习。

## 与 S2ST 的联系和自测

[Whisper](../03-模型研究/Whisper.md)解码文字，[NLLB](../03-模型研究/NLLB-200.md)解码译文，[S2UT](../03-模型研究/S2UT.md)解码语音 units；接口不同，但都可用条件序列建模理解。

- 为什么 `[B, Ty, V]` 的 V 轴不是声道数？
- 把语音帧数减半会怎样影响注意力计算和细节？
- 为什么“训练准确率高”不能保证长序列生成稳定？

基础来源：[Attention Is All You Need](https://arxiv.org/abs/1706.03762)。下一层可补 RNN、CTC 与对齐，不要求现在推导所有层的梯度。
