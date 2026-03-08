<h1 align="center">
Homepage Template
</h1>

<div align="center">

An agent-friendly Jekyll homepage template for academic and professional profiles.

[中文文档](./docs/README-zh.md)
</div>

<p align="center">
  <img src="docs/template-preview.svg" width="100%" alt="Template preview" />
</p>

## Why this repo exists

This repository is the **public template release** extracted from a private, continuously customized personal homepage.

- It keeps the reusable layout, sections, and deployment workflow.
- It removes private content, private data exports, and personal-only assets.
- It is designed to be easy for both humans and coding agents to adapt.

## Live demo

- Production example: https://amberheart.github.io/
- Template repository: this public repo ships with placeholder content only

The deployed example above contains real personal content and ongoing customizations. This template repository does **not** include the private source repository behind that site.

## What this template includes

- Single-page homepage with sidebar profile and anchored navigation
- Sections for About, News, Experience, Education, Publications, Projects, Awards, and Service
- Optional Google Scholar citation sync via GitHub Actions
- Optional CV download entry and media placeholders
- GitHub Pages deployment workflow
- Public-safe placeholder content for quick forking and remixing

## Quick start

Need a coding-agent-oriented handoff? See [`docs/agent-setup.md`](./docs/agent-setup.md).


1. Fork this repository.
2. If you want a GitHub user site, rename the repo to `USERNAME.github.io`.
3. If you keep it as a project repo, set `url` and `baseurl` in `_config.yml`.
4. Update `_config.yml` with your name, bio, links, avatar, and optional CV path.
4. Replace the sample content in `_pages/about.md`.
5. Replace placeholder assets in `images/`, `videos/`, and `CV/` as needed.
6. Run the site locally, verify the build, then publish with GitHub Pages.

## Local development

```bash
bundle install
bash run_server.sh
```

Open `http://127.0.0.1:4000` in your browser.

To validate a production-style build:

```bash
bundle exec jekyll build
```

## Optional Google Scholar setup

If you want automatic citation data:

1. Find your Google Scholar user ID.
2. Add `GOOGLE_SCHOLAR_ID` in `Settings -> Secrets and variables -> Actions`.
3. Enable `.github/workflows/google_scholar_crawler.yaml`.
4. Optionally show citation counts in your own content with:

   ```html
   <span class='show_paper_citations' data='YOUR_PAPER_ID'></span>
   ```

If the secret is not configured, the workflow is skipped.

## Files you will likely edit first

- `_config.yml` — site metadata, author profile, social links, optional CV path
- `_pages/about.md` — homepage structure and section content
- `images/` — avatar, logos, project thumbnails, favicon assets
- `videos/` — optional demo clips for projects or papers
- `CV/` — optional CV source and exported PDF

## Reuse and attribution

This template supports heavy customization and remixing, but reuse should keep the relevant upstream attribution.

- Homepage base: [RayeRen/acad-homepage.github.io](https://github.com/RayeRen/acad-homepage.github.io)
- CV format inspiration and original LaTeX source lineage: Jake Gutierrez's "Jake's Resume"

If you redistribute substantial portions of this template or derived templates, keep the upstream license and attribution notices.

## License

MIT. See `LICENSE`.
