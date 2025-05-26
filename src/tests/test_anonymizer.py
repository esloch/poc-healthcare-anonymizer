import pytest
from healthcare_anonymizer.anonymizer import HealthcareAnonymizer


@pytest.fixture
def anonymizer():
    return HealthcareAnonymizer()


def test_anonymization_with_location(anonymizer):
    text = (
        "John Doe lives in New York and his email is john@example.com. "
        "The appointment was on 12/03/2023."
    )
    result = anonymizer.anonymize_text(text)

    assert "John Doe" not in result
    assert "john@example.com" not in result
    assert "New York" not in result
    assert "12/03/2023" not in result
    assert "<REDACTED>" in result
