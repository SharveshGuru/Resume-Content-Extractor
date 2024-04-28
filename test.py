import nltk
import spacy.cli

def exec():
    nltk.download('stopwords')
    spacy.cli.download('en_core_web_sm')