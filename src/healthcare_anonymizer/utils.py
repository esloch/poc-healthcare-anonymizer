def clean_text(text: str) -> str:
    """
    Cleans the input text by removing unnecessary whitespaces and newlines.

    Args:
        text (str): The input text.

    Returns:
        str: Cleaned text.
    """
    return text.strip().replace('\n', ' ')
