FROM python:3.10-slim-buster

ARG TARGETARCH

# Install tini and create an unprivileged user
ADD https://github.com/krallin/tini/releases/download/v0.19.0/tini-${TARGETARCH} /sbin/tini
RUN addgroup --gid 1002 "gate" && \
      adduser --disabled-password --gecos "GATE User,,," \
      --home /gate --ingroup gate --uid 1002 gate && \
      chmod +x /sbin/tini

RUN pip install Flask Flask-API gunicorn

COPY --chown=gate:gate app.py /gate/
USER gate:gate
WORKDIR /gate
CMD ["/sbin/tini", "--", "gunicorn"  , "--bind", "0.0.0.0:8000", "app:app"]
