# S2ST 研究笔记与实验代码

本仓库包含两个部分，统一通过当前 STS 根目录管理 Git 版本。

| 目录 | 用途 | 入口 |
| --- | --- | --- |
| `01 STS_NOTE/` | Obsidian 笔记库、论文阅读与研究记录 | [首页](01%20STS_NOTE/首页.md) · [科研知识库](01%20STS_NOTE/S2ST-Research/README.md) |
| `02 STS_CODE/` | Python 实验代码、配置与示例 | [实验代码说明](02%20STS_CODE/S2ST-Research/README.md) |

在 Obsidian 中选择“打开本地仓库”，打开 `01 STS_NOTE` 文件夹。笔记库设置与主题随仓库保存；社区插件安装文件、插件本地数据和工作区状态不提交，需要时根据 `.obsidian/community-plugins.json` 在 Obsidian 中重新安装插件。

模型权重、实际数据集、私人录音、实验输出、Python 环境与缓存不提交。数据与输出目录中的 README 和示例配置仍保留在仓库中。

## 后续同步

在当前 STS 根目录打开终端。开始编辑前拉取远程更新：

```powershell
git pull --ff-only
```

完成编辑后检查并提交：

```powershell
git status
git add .
git commit -m "Update research notes and code"
git push
```

仓库地址：<https://github.com/FisherGoGo/S2ST->。以上为手动同步，不会自动定时上传。
