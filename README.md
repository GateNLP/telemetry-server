# GATE telemetry server

Receives calls containing JSON, performs (very) simple validation and prints JSON to stdout along with the time and source IP of the call.

**Privacy note**: if you are using this app to collect telemetry you should consider carefully whether and for how long to retain the IP addresses, and ensure this is covered in your privacy policy.  In the case of the standard GATE Team telemetry collector:

- _raw_ IP addresses are retained for a maximum of 14-21 days in web server logs for technical and operation reasons (e.g. to monitor for and mitigate denial of service attacks)
- actual telemetry data is retained for longer but this does not include the raw IP addresses, only aggregated data at the level of city & country obtained by [IP geo-location](https://www.elastic.co/guide/en/elasticsearch/reference/master/geoip-processor.html)

## How to use the tool

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
