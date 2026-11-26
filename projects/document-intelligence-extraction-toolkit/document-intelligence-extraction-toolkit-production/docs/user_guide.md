# User guide

1. Start the API locally or with Docker Compose.
2. Open `/docs` and select `POST /api/v1/extract`.
3. Upload one TXT, MD, CSV or text-based PDF file.
4. Review extracted text, word/character counts, headings, email addresses and URLs.

The endpoint returns one document per request. Batch orchestration can be implemented by calling the endpoint for each file. OCR and image-only PDF extraction are not supported.
