# GATE telemetry server

Receives calls containing JSON, performs (very) simple validation and prints JSON to stdout.

Build the image:

```
docker build -t telemetry:latest .
```

Launch the image:

```
docker run -p 8000:8000 -d telemetry:latest
```

## Testing
pytest is required for testing, you can install it with `pip install pytest`

To test, launch the container as above and run pytest with `pytest`