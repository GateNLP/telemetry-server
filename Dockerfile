FROM python:3.10-slim-buster

COPY app.py .
RUN pip install Flask Flask-API gunicorn
CMD ["gunicorn"  , "--bind", "0.0.0.0:8000", "app:app"]
