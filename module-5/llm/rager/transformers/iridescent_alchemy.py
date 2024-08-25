import spacy
from typing import List, Tuple


# Function to load the spaCy model based on the language provided in kwargs
def load_spacy_model(language: str):
    models = {
        'en': 'en_core_web_sm',
        'de': 'de_core_news_sm',
        'es': 'es_core_news_sm'
        # Add more languages and their corresponding spaCy models as needed
    }
    return spacy.load(models.get(language, 'en_core_web_sm'))  # Default to English model if not found

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def sentence_tokenization(document_data: Tuple[str, str, str], *args, **kwargs) -> Tuple[str, str, str, List[str]]:
    """
    Tokenize text into sentences using spaCy.

    Args:
        document_data (Tuple[str, str, str]): Tuple containing document_id, document_content, and chunk.
    Returns:
        Tuple[str, str, str, List[str]]: Tuple containing document_id, document_content, chunk, and tokenized sentences.
    """
    document_id, document_content, chunk = document_data
    language = kwargs.get('language', 'en')
    nlp = load_spacy_model(language)

    # Process the text chunk using spaCy for sentence tokenization
    doc = nlp(chunk)
    sentences = [sent.text for sent in doc.sents]

    return document_id, document_content, chunk, sentences


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'