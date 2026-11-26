FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml README.md ./
COPY src ./src
RUN pip install --no-cache-dir .
RUN useradd --create-home appuser
USER appuser
CMD ["python", "-c", "print('API Integration Toolkit installed. Import api_integration.pipeline to build a validated integration.')"]
