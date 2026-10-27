# S2ST 实验代码

Python 实验与 Obsidian 正文分开存储，共用当前 STS 项目。笔记入口：[科研知识库](../../01%20STS_NOTE/S2ST-Research/README.md)，第一次操作：[第一次实践](../../01%20STS_NOTE/S2ST-Research/07-实验/第一次实践.md)。

## 本机 s2st GPU 环境

2026-10-27 已在 `D:\Tools\Miniconda\envs\s2st` 配置 Python 3.11.18、PyTorch/TorchAudio 2.9.1（CUDA 12.8）、ipykernel、NumPy、SciPy、pandas、Matplotlib、librosa 和 SoundFile。VS Code Notebook 右上角选择 `Python (s2st GPU)`；终端使用 `conda activate s2st`。

已通过实际 Jupyter 内核启动、RTX 4070 Laptop GPU 矩阵运算、GPU 音频重采样、STFT、WAV 读写、绘图和 `pip check`。环境激活变量和内核配置均设置 `PYTHONNOUSERSITE=1`，已检查主要包均来自本环境。模型推理需按下方说明另行准备具体模型依赖和 checkpoint。

[environment.s2st.yml](environment.s2st.yml) 固定本次安装的直接依赖，供 Windows GPU 环境重建；传递依赖未完整锁定。在本目录执行：

```powershell
conda env create --prefix 'D:\Tools\Miniconda\envs\s2st' --file environment.s2st.yml
conda activate s2st
python -m ipykernel install --user --name s2st --display-name 'Python (s2st GPU)' --env PYTHONNOUSERSITE 1
```

重建命令用于目标环境尚不存在时。日常使用只需激活环境或选择上述内核。

```text
configs/                  配置示例；尚未绑定真实 checkpoint
data/                     样本格式说明与无音频元数据示例
models/                   模型下载约定（未下载）
runs/                     不覆盖的真实输出记录（默认不入 Git）
src/s2st_lab/audio.py      PCM16 WAV 检查、hash、JSON 写入
scripts/inspect_audio.py  标准库音频检查入口
scripts/create_run.py     仅创建记录，不执行级联
scripts/transcribe_whisper.py  可选本地 Whisper 推理示例
scripts/check_kb.py        Markdown/Wikilink 本地目标检查
adapters/README.md        MT/TTS/统一式模型待实现接口
```

## 立即可运行：不安装依赖

在 PowerShell 中：

```powershell
Set-Location -LiteralPath 'D:\Project\Note\Science\STS\02 STS_CODE\S2ST-Research'
python scripts/inspect_audio.py --help
python scripts/create_run.py --help
python scripts/check_kb.py --kb '..\..\01 STS_NOTE\S2ST-Research'
python scripts/inspect_audio.py --input 'D:\你的录音\sample.wav' --output 'audio-check.json'
python scripts/create_run.py --input 'D:\你的录音\sample.wav' --config configs/cascade.example.json --output runs/exp-001
```

检查工具只接受未压缩 16-bit PCM WAV，按块读入，保存幅值诊断与 SHA256，不修改输入。其他格式要另行、显式地转换。`create_run.py` 保存配置、输入检查和 Python/OS/Git 等记录，阶段均为 `not_run`，不是一次完整翻译。

## 可选：真实 Whisper 示例

该脚本未在真实模型上执行，本次只检查语法和 CLI。先按[资源文档](../../01%20STS_NOTE/S2ST-Research/07-实验/环境与资源准备.md)准备独立环境、PyTorch、官方 `openai-whisper` 包、FFmpeg 与已有本地 checkpoint。不要把本页当作已经验证过的全组件安装锁文件。不会在导入或 `--help` 时安装依赖、访问网络或加载模型。

```powershell
python scripts/transcribe_whisper.py --input 'D:\你的录音\sample.wav' --checkpoint 'D:\模型目录\tiny.pt' --language zh --device cpu --output runs/exp-001/source_asr.json
```

输入为本地音频和明确存在的 `.pt` 路径；输出 UTF-8 JSON 含转写、分段、模型与输入 hash、版本、参数和耗时。模型对象通过官方 `whisper.load_model` 的本地路径分支加载，脚本不提供按模型名下载的分支。仅用可信来源的权重。此示例只做 ASR `transcribe`；MT/TTS/统一模型和指标尚未实现。

所有输出拒绝覆盖；同一个实验修改参数请建新目录。实际输入、模型、生成音频、run.json 默认不提交 Git；可分享的研究结论和必要配置以笔记提交，保留日志路径与哈希。
