import re
import spacy
nlp = spacy.load("en_core_web_lg")

def clean_text(text):
    """
    Clean and preprocess the input text.

    This function tokenizes the input text, converts tokens to lowercase,
    removes punctuation, and ensures that the text only contains letters,
    digits, and whitespace.

    Args:
        text (str): The input text to be cleaned.

    Returns:
        str: The cleaned and preprocessed text.
    """
    doc = nlp(text)
    cleaned_text = ' '.join(token.text.lower() for token in doc if not token.is_punct)
    cleaned_text = re.sub(r'\s+', ' ', re.sub(r'[^a-zA-Z0-9\s]', '', cleaned_text)).strip()
    return cleaned_text

def remove_stopwords(text):
    """
    Remove stopwords from the input text.

    Args:
        text (str): The input text from which stopwords will be removed.

    Returns:
        str: The cleaned text with stopwords removed.
    """
    doc = nlp(text)
    cleaned_text = ' '.join(token.text for token in doc if not token.is_stop)
    return cleaned_text
