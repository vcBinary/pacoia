import re
from collections import Counter
from operator import itemgetter

import textstat
from lexicalrichness import LexicalRichness

from src.model.text import TextAnalyzer


def get_words(text: str) -> list[str]:
    return re.findall(r"\b\w+(?:[-']\w+)*\b", text)


def get_words_distribution(text: str) -> dict[str, int]:
    words = TextAnalyzer.get_words(text)
    lower_case_words = [re.sub(r"[^\w\s']", "", w.lower()) for w in words]
    frequencies = Counter(lower_case_words)
    return dict(sorted(frequencies.items(), key=itemgetter(1), reverse=True))

# Readability Metrics


def get_flesch_reading_ease(text: str) -> float:
    return textstat.flesch_reading_ease(text)


def get_flesch_kincaid_grade(text: str) -> float:
    return textstat.flesch_kincaid_grade(text)


def get_smog_index(text: str) -> float:
    return textstat.smog_index(text)


def get_dale_chall_readability_score(text: str) -> float:
    return textstat.dale_chall_readability_score(text)


# Lexical Richness Metrics

def get_cttr(lex: LexicalRichness) -> float:
    return lex.cttr


def get_herdan(lex: LexicalRichness) -> float:
    return lex.Herdan


def get_yulek(lex: LexicalRichness) -> float:
    return lex.yulek


def get_simpsond(lex: LexicalRichness) -> float:
    return lex.simpsond
