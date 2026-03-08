# Agent Setup Guide

This repository is intended to be easy for coding agents to adapt without accessing any private source repository.

## Primary edit targets

- `_config.yml`: identity, links, avatar, optional CV path, repo metadata
- `_pages/about.md`: homepage sections and the majority of visible content
- `images/`: avatar, logos, thumbnails, favicon assets
- `videos/`: optional project or paper demo clips
- `CV/`: optional CV source and exported PDF

## Safe workflow

1. Read `AGENTS.md` first.
2. Update `_config.yml` before editing visible content.
3. Replace placeholder content in `_pages/about.md`.
4. Replace placeholder assets only after the content structure is stable.
5. Run a local build before proposing a release.

## Commands

```bash
bundle install
bash run_server.sh
bundle exec jekyll build
```

## Public-template constraints

- Do not add private datasets, private exports, or personal-only assets.
- Do not commit `_site/`, local bundles, or generated cache directories.
- Keep attribution to the upstream homepage base and CV lineage.
- Prefer minimal, reviewable edits over broad rewrites.

## Reuse notes

- Homepage base: `RayeRen/acad-homepage.github.io`
- CV lineage: Jake Gutierrez's `Jake's Resume`
- Live production example: `https://amberheart.github.io/`

Use the live site as a styling and content example, but treat this repository as the only public source of truth for the template.
