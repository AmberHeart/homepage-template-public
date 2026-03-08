# Repository Guidelines

## Project Structure & Module Organization
This site is a Jekyll-based academic homepage. Put page content in `_pages/`, shared templates in `_layouts/` and `_includes/`, and theme styles in `_sass/` plus `assets/css/`. Frontend scripts live in `assets/js/`, while static media belongs in `images/`, `videos/`, and `CV/`. Automation for citation syncing lives in `google_scholar_crawler/`, with generated JSON stored in `google_scholar_data/`. Treat `_site/` as build output: review it locally if needed, but do not hand-edit generated files there.

## Build, Test, and Development Commands
- `bundle install` — install Ruby gems from `Gemfile`.
- `bash run_server.sh` — start the local Jekyll live-reload server at `http://127.0.0.1:4000`.
- `bundle exec jekyll build` — perform a production-style site build into `_site/`.
- `cd google_scholar_crawler && pip install -r requirements.txt && python main.py` — run the citation crawler manually when debugging scholar data updates.

## Coding Style & Naming Conventions
Follow the existing repository style instead of introducing a new one. Use 2-space indentation in YAML and Liquid-heavy content files, keep Markdown headings concise, and prefer descriptive kebab-case or snake_case names that match surrounding files. Update source assets such as `assets/js/_main.js` or `assets/css/main.scss`; do not edit generated or minified outputs unless the source file is unavailable. Keep homepage content changes focused in `_pages/about.md` and configuration changes in `_config.yml`.

## Testing Guidelines
There is no formal unit-test suite in this repository. For every content or styling change, run `bundle exec jekyll build` first, then inspect the page locally with `bash run_server.sh`. When touching the citation pipeline, verify that refreshed files in `google_scholar_data/` are valid JSON and that the homepage still renders without missing badge data.

## Commit & Pull Request Guidelines
Recent history favors short, imperative commits, with Conventional Commit-style prefixes used for meaningful changes: `feat:`, `fix:`, and `chore:`. Prefer `fix: update scholar badge path` over vague messages like `update`. Pull requests should include: a short summary, the main files changed, linked issues if applicable, and screenshots for visible homepage or layout updates. Note any config or secret requirements, especially changes related to GitHub Pages or scholar crawling.

## Security & Configuration Tips
Keep secrets such as `GOOGLE_SCHOLAR_ID` in GitHub Actions secrets, not in tracked files. Review `.github/workflows/` before changing deployment or crawler behavior, and document any new required environment variables in `README.md`.
