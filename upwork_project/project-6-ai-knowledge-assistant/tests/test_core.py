from knowledge_assistant.core import Passage, answer_from_evidence, split_passages

def test_chunking_preserves_document_and_order():
    chunks = split_passages(" ".join(["policy"] * 250), "handbook.txt", 100)
    assert len(chunks) == 3
    assert chunks[0].document == "handbook.txt"
    assert chunks[0].ordinal == 1

def test_answer_contains_traceable_evidence():
    passages = [Passage("leave.md", "Annual leave requests require manager approval.", 1)]
    result = answer_from_evidence("Who approves annual leave requests?", passages)
    assert "manager approval" in result.answer
    assert result.sources[0].document == "leave.md"
    assert result.needs_review is False

def test_abstains_when_no_evidence():
    result = answer_from_evidence("What is the office parking policy?", [
        Passage("travel.txt", "Expenses are submitted monthly.", 1)
    ])
    assert result.needs_review is True
    assert not result.sources
