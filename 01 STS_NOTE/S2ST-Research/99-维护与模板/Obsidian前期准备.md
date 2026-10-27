---
type: maintenance
status: 初稿
created: 2026-10-27
updated: 2026-10-27
tags:
  - s2st
---

# Obsidian 前期准备

## 当前仓库已经有什么

请继续把 **`D:\Project\Note\Science\STS\01 STS_NOTE`** 作为仓库打开。不要把 `S2ST-Research` 再创建成嵌套仓库，否则仓库根路径链接和配置会混乱。

本次检查发现已有 `.obsidian`：核心 Templates、双链、属性、搜索、关系图、文件恢复等已启用，文件移动自动更新链接为开启；社区插件当前启用清单为 quick-latex、obsidian-style-settings、better-export-pdf。其他插件文件存在不代表已启用。本次没有安装插件或改主题、启用清单、workspace 和已有 app 设置。

## 已实际完成的轻量准备

- 新建仓库根的 `首页.md`，链接知识地图、模型/论文索引、实验入口和维护说明；可以手动设书签。
- 新增 `S2ST-Research/99-维护与模板/模板` 的三个统一模板；原先没有 `templates.json`，本次仅新建该配置，指向这个目录。
- 笔记使用扁平 YAML 属性 `type/status/created/updated/tags`；模板日期带引号。模型和论文独立保存证据，避免多处改作者/年份。
- 普通正文使用 Markdown 相对链接，兼容仓库外阅读；模板中的固定导航使用带完整仓库路径的 Wikilink，插入任意子目录仍能解析。
- 新建 `09-附件` 说明，但不自动改变已有默认附件位置，不移动现有插件文件。

## 值得你在软件里做的设置

1. 打开首页并加入书签；试用悬浮预览、反向链接和本地关系图，不必首先整理全局大图。
2. 在“文件与链接”确认新链接采用相对路径、自动更新内部链接保持开启。Obsidian 支持 Markdown 和 Wikilink，两种都能建立反链；不需要为了用 Obsidian 重写所有正文。
3. 若想统一科研截图，可把新附件位置设为指定目录 `S2ST-Research/09-附件`，按 `paper_id-figure-purpose` 命名；论文 PDF 建议在 Zotero/外部文献目录管理，并在笔记记录来源、页码与可访问位置。
4. 核心 Templates 已指向模板文件夹，创建一个测试笔记后插入模型模板，确认日期、标题和导航。若软件正在运行未刷新，重新打开仓库后检查。
5. 现有 `promptDelete` 为 false；可自行决定开启删除确认。这里只提示实际设置，没有修改你的偏好。

## 插件先保持少量

本库无需 Dataview、Templater、Excalidraw 或 Mermaid 插件即可阅读和维护。核心 Markdown、LaTeX、Mermaid、属性和 Templates 足够起步。需要图像手绘或大量文献同步时再按真实需要选择工具，先备份再试；本次不安装、不启用已有未启用插件。

项目位于上层已有 Git 仓库中。本次只新增局部 ignore，没有初始化新仓库或提交。Obsidian Git 插件已存在但不在当前启用清单，暂时用手动 Git/现有备份方式即可。不要同时启用多个双向同步工具同步同一目录；同步与有历史版本的备份分别考虑。

## 每新增一页先做什么

已有概念则补充原页；新概念给它一个明确问题、至少一条相关笔记链接和准确状态；新论文先分配稳定 ID 再建卡；新实验保留失败和真实命令。详见[维护规范](知识库维护规范.md)。

官方依据：[内部链接](https://obsidian.md/help/links)、[Templates](https://obsidian.md/help/plugins/templates)、[Properties](https://obsidian.md/help/properties)。上述软件设置步骤未做 GUI 点击验证，现有 JSON 状态与新增文件已离线检查。
