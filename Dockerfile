FROM python:3.10-slim
WORKDIR /app
COPY ./celery_app /app
RUN pip install celery
CMD ["celery", "-A", "tasks", "worker", "--loglevel=info"]
