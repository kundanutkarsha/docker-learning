FROM python:3.12-alpine

WORKDIR /app

RUN adduser -D appuser

USER appuser

COPY app.py .

CMD ["python", "app.py"]
