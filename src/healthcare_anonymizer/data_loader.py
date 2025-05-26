import pandas as pd
from pathlib import Path

CLINICAL_NOTES = Path(__file__).parent.parent / "data" / "clinical_notes.csv"

def load_mock_data(filepath: str = CLINICAL_NOTES) -> pd.DataFrame:
    """
    Load mock clinical note data from a CSV file.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the clinical notes.
    """
    return pd.read_csv(filepath)
