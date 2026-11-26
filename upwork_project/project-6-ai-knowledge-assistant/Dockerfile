FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml README.md ./
COPY src ./src
RUN pip install --no-cache-dir ".[api]"
RUN useradd --create-home appuser
USER appuser
CMD ["uvicorn", "knowledge_assistant.api:app", "--host", "0.0.0.0", "--port", "8000"]
