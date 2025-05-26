from healthcare_anonymizer.utils import clean_text


def test_clean_text():
    dirty = "  This is a test.\n"
    cleaned = clean_text(dirty)
    assert cleaned == "This is a test."
