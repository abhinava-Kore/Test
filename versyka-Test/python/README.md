# Python upgrade fixture

A deliberately small Python environment for checking dependency vulnerability findings, major upgrades, source edits, and transitive compatibility. It is separate from the Node.js fixture in the parent folder.

## Intentional upgrade seams

- `BaseSettings` is imported from `pydantic`, and the nested `Config` class uses Pydantic v1 settings conventions. Moving to Pydantic 2 requires the `pydantic-settings` package and source changes.
- FastAPI 0.95.2 requires Pydantic below 2, so upgrading Pydantic alone creates a resolver conflict. Upgrade FastAPI and Pydantic as a compatible set.
- `torch==2.1.0` and `torchvision==0.16.0` are a matched pair. Update them together to a compatible pair rather than changing only one pin.
- `request.dict()` is the Pydantic v1 serialization call and should be migrated to the v2 API when upgrading.

The project pins are intentionally old for a disposable scan fixture. It does not download a model until the app is started. Do not treat these versions as production recommendations.

## Resolve the lockfile

```sh
uv lock
```

## Run

```sh
uv sync
uv run uvicorn versyka_fixture.app:app --app-dir src
```

The HTTP app loads the default text-classification model on startup, so running it may download model files. The dependency scan itself does not need to start the app.
