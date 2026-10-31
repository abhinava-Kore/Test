# Versyka upgrade test fixtures

This folder contains two independent projects for evaluating dependency vulnerability findings and upgrade-generated source fixes:

- `node/` — pnpm fixture with pinned Node.js dependencies and `pnpm-lock.yaml`.
- `python/` — uv fixture with `pyproject.toml` and Python source.

The dependency pins and compatibility seams are intentionally old. Scan these fixtures before upgrading them. They are test scaffolds, not production recommendations.
