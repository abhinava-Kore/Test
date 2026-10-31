# Versyka dependency upgrade fixture

A small Node.js service pinned to old dependencies for testing dependency vulnerability detection and major-version upgrade recommendations. The Express 4 wildcard route is an intentional compatibility seam for an Express 5 upgrade.

This is a local evaluation scaffold, not a checkout of `abhinava-Kore/versyka-Test`.

## Run

Requires Node.js 18+ and pnpm 11.13.0.

```sh
pnpm install --frozen-lockfile
pnpm start -- --port 3000
```

Try `GET /health` and `GET /files/reports/summary`. Keep the dependency versions pinned through the initial Versyka scan; apply its proposed updates afterward.
