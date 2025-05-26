from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig


class HealthcareAnonymizer:
    """
    A class to anonymize clinical text containing personal identifiable information (PII).
    """

    def __init__(self):
        self.analyzer = AnalyzerEngine()
        self.anonymizer = AnonymizerEngine()

    def anonymize_text(self, text: str) -> str:
        """
        Anonymizes the input text by detecting and replacing PII with <REDACTED>.

        Args:
            text (str): The text to be anonymized.

        Returns:
            str: The anonymized text.
        """
        results = self.analyzer.analyze(
            text=text,
            entities=["PERSON", "EMAIL_ADDRESS", "PHONE_NUMBER", "DATE_TIME", "LOCATION"],
            language="en"
        )

        operators = {
            "DEFAULT": OperatorConfig(operator_name="replace", params={"new_value": "<REDACTED>"})
        }

        anonymized_result = self.anonymizer.anonymize(
            text=text,
            analyzer_results=results,
            operators=operators
        )

        return anonymized_result.text
