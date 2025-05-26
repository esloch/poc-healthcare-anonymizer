"""
Configuration constants for the Healthcare Anonymizer project.
"""

SUPPORTED_ENTITIES = [
    "PERSON",
    "EMAIL_ADDRESS",
    "PHONE_NUMBER",
    "DATE_TIME",
    "LOCATION"
]

REPLACEMENT_STRING = "<REDACTED>"
