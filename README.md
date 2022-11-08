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