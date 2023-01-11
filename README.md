# GATE telemetry server

Receives calls containing JSON, performs (very) simple validation and prints JSON to stdout.

You can run a pre-built image from `ghcr.io`:

```
docker run -p 8000:8000 -d ghcr.io/gatenlp/telemetry-server:main
```

or for local development you can build the image yourself:

```
docker buildx build -t telemetry:latest .
```

and then run it using:

```
docker run -p 8000:8000 -d telemetry:latest
```

## Testing
pytest is required for testing, you can install it with `pip install pytest`

To test, launch the container as above and run pytest with `pytest`
