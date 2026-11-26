from document_intelligence.engine.extractor import extract_bytes

def extract_document(filename: str, content: bytes) -> dict:
    return extract_bytes(filename, content)
