---
type: experiment-guide
status: 初稿
created: 2026-10-27
updated: 2026-10-27
tags:
  - s2st
---

# 实验入口

**第一次操作打开[第一次实践](第一次实践.md)。** 先用 Python 标准库检查自有 PCM16 WAV，再决定隔离环境与 Whisper 权重；本次未下载任何模型。

## 文档与源码分工

- 本目录：方案、实验记录、数据和评价约定。
- 代码：[README](../../../02%20STS_CODE/S2ST-Research/README.md)；绝对位置 `D:\Project\Note\Science\STS\02 STS_CODE\S2ST-Research`。
- Obsidian 的搜索、双链和附件默认限于 `01 STS_NOTE`；外部 Python 文件用终端/代码编辑器打开，勿建指向外部代码的伪 Wikilink 或嵌套 vault。

## 当前实际能力

1. `inspect_audio.py`：本地 PCM16 WAV 元数据与幅值诊断；标准库即可运行，不修改输入。
2. `create_run.py`：创建不覆盖的运行目录，保存输入 hash、配置和基础环境，作为实验追踪起点。
3. `transcribe_whisper.py`：可选最小真实 ASR 示例，**要求已有本地 .pt checkpoint 和依赖**；不会根据模型名联网下载。只完成语法/CLI 检查，未执行真实模型。
4. `check_kb.py`：验证 Markdown 相对链接和本库 Wikilink 目标，可在文档更新后运行。

MT、TTS、完整级联、统一式推理和自动评价当前是文档/接口骨架，未提供可假装成功的模型桩或模拟质量分数。按[实验路线与比较协议](实验路线与比较协议.md)逐项实现。未来真实推理可分环境运行，通过 UTF-8 文本、WAV 和 JSON 交接，不强求所有历史项目装进同一个环境。

记录用[实验记录模板](实验记录模板.md)，环境与资源判断见[环境与资源准备](环境与资源准备.md)。
