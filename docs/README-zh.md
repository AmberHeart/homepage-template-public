<h1 align="center">
Homepage Template
</h1>

<div align="center">

一个对 coding agent 友好的 Jekyll 个人主页模板，适合学术主页或职业展示页。

[English README](../README.md)
</div>

<p align="center">
  <img src="./template-preview.svg" width="100%" alt="模板预览图" />
</p>

## 这个仓库为什么存在

这个仓库是从一个持续演化的私有个人主页中抽取出来的 **公开模板版本**。

- 保留了可复用的布局、区块结构和部署流程。
- 去掉了私有内容、私有数据导出和仅个人可用的素材。
- 默认面向人类用户和 coding agent 都能快速接手。

## 参考链接

- 我的真实个人主页：https://amberheart.github.io/
- 原始公开主页仓库地址：https://github.com/RayeRen/acad-homepage.github.io

上面的个人主页包含真实内容和持续魔改；这个 public template repo 只提供公开安全的占位内容。

## 展示图

### 模板截图

![Template homepage screenshot](./template-homepage.png)

## 模板包含什么

- 单页主页布局，带侧边栏个人信息和锚点导航
- About、News、Experience、Education、Publications、Projects、Awards、Service 等常用区块
- 可选 Google Scholar 引用统计同步
- 可选 CV 下载入口和媒体占位资源
- 可选 GitHub Pages 部署工作流
- 适合 fork 和二次魔改的中性占位内容

## 快速开始

如果你准备交给 coding agent 直接接手，先看 [`docs/agent-setup.md`](./agent-setup.md)。


1. Fork 本仓库。
2. 如果你要发布 GitHub 用户主页，建议把仓库名改成 `USERNAME.github.io`。
3. 如果你保留 project repo 形式，请在 `_config.yml` 中设置 `url` 和 `baseurl`。
4. 修改 `_config.yml`，填入你的姓名、简介、链接、头像和可选 CV 路径。
4. 修改 `_pages/about.md` 中的示例内容。
5. 按需替换 `images/`、`videos/`、`CV/` 下的占位资源。
6. 本地运行并验证生成出来的 `_site` 目录。
7. 如果你需要公开托管，请在你自己的 fork 中启用 GitHub Pages，并手动运行 Pages workflow。

## 本地开发

```bash
bundle install
bash run_server.sh
```

然后在浏览器打开 `http://127.0.0.1:4000`。

如需做一次接近生产环境的构建检查：

```bash
bundle exec jekyll build
```

## 可选的 Google Scholar 配置

如果你希望自动同步引用数：

1. 找到你的 Google Scholar user ID。
2. 在仓库 `Settings -> Secrets and variables -> Actions` 中添加 `GOOGLE_SCHOLAR_ID`。
3. 启用 `.github/workflows/google_scholar_crawler.yaml`。
4. 如需在页面中显示单篇论文引用数，可在内容中加入：

   ```html
   <span class='show_paper_citations' data='YOUR_PAPER_ID'></span>
   ```

如果没有配置 secret，workflow 会直接跳过。

## 最先建议修改的文件

- `_config.yml`：站点信息、作者资料、社交链接、可选 CV 路径
- `_pages/about.md`：主页内容和区块结构
- `images/`：头像、logo、项目缩略图、favicon 等资源
- `videos/`：可选项目或论文演示视频
- `CV/`：可选简历源码和导出的 PDF

## 二次使用与标注

这个模板支持较大幅度的二次魔改，但复用时应保留相关上游来源标注。

- 原始公开主页仓库地址：`https://github.com/RayeRen/acad-homepage.github.io`
- CV 版式灵感与原始 LaTeX 来源链路：Jake Gutierrez 的 `Jake's Resume`

如果你分发本模板或其衍生模板的主要部分，请保留上游许可证和来源说明。

## 许可证

MIT，见 `LICENSE`。
