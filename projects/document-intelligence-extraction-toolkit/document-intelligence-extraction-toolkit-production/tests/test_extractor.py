from document_intelligence.engine.extractor import extract_bytes

def test_markdown_metadata():
    result = extract_bytes("readme.md", b"# Overview\nContact test@example.com https://example.org")
    assert result["headings"] == ["Overview"]
    assert result["emails"] == ["test@example.com"]
    assert result["urls"] == ["https://example.org"]
    assert result["word_count"] == 8

def test_csv_text_conversion():
    result = extract_bytes("rows.csv", b"name,value\nalpha,10")
    assert "alpha | 10" in result["text"]

def test_reject_unknown_extension():
    try:
        extract_bytes("bad.exe", b"no")
    except ValueError as exc:
        assert "Unsupported" in str(exc)
    else:
        raise AssertionError("Expected unsupported extension error")
