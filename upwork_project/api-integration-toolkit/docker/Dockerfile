FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml README.md ./
COPY src ./src
RUN pip install --no-cache-dir ".[http]" && useradd --create-home appuser
USER appuser
CMD ["python", "-c", "print('Integration library ready; supply a reviewed provider-specific worker entry point.')"]
