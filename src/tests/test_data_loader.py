from healthcare_anonymizer.data_loader import load_mock_data
from pathlib import Path

CLINICAL_NOTES = Path(__file__).parent.parent / "data" / "clinical_notes.csv"


def test_load_mock_data():
    df = load_mock_data(filepath=CLINICAL_NOTES)
    assert not df.empty
    assert "patient_id" in df.columns
    assert "note" in df.columns
