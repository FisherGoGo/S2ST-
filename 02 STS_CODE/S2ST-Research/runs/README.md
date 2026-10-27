# 运行目录

每次真实运行选择新的 `exp-xxx` 目录。建议产物：`run.json`、`input.json`、`config.json`、`source_asr.json`、`source_text.txt`、`target_text.txt`、`tts_input.txt`、`output.wav`、`metrics.json`、`stderr.log`。只创建实际产生的文件。

`create_run.py` 当前仅生成前三项并将所有模型阶段标记 not_run。未运行指标为 null，不用 0 替代。失败保留目录和日志；每个研究判断在 Obsidian 中链接对应记录。默认不提交运行产物，但要保存可审查副本并记录其 hash/配置。
