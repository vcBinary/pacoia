import numpy as np
from lexicalrichness import LexicalRichness

from src.model.text import LexicalRichnessConstants as LexRichCons
from src.model.text import ReadabilityConstants as ReadCons
from src.model.text import TextAnalyzer

SMALL_WORD_MAX_LETTERS = 3


def get_words_distribution_feedback(word_frequencies: dict[str, int]) -> str:
    total_words = sum(list(word_frequencies.values()))
    percentile = np.percentile(list(word_frequencies.values()), 80)
    feedback = ""

    for word, count in word_frequencies.items():
        pct = (count / total_words) * 100
        if count > percentile and len(word) > SMALL_WORD_MAX_LETTERS:
            feedback += f"⚠️ You used the word **'{word}'** {count} times ({pct:.1f}%). Consider using it less.\n"

    return feedback


def get_lexical_richness_feedback(text: str) -> str:
    lex = LexicalRichness(text)

    feedback = "## 🧠 Lexical Richness Metrics\n\n"

    cttr = TextAnalyzer.get_cttr(lex)
    feedback += f"**Corrected Type-Token Ratio (CTTR):** {cttr:.2f}"
    feedback += get_cttr_feedback(cttr)

    yulek = TextAnalyzer.get_yulek(lex)
    feedback += f"**Yule's K:** {yulek:.2f}"
    feedback += get_yulek_feedback(yulek)

    simpsond = TextAnalyzer.get_simpsond(lex)
    feedback += f"**Simpson's D:** {simpsond:.2f}"
    feedback += get_simpsond_feedback(simpsond)

    herdan = TextAnalyzer.get_herdan(lex)
    feedback += f"**Herdan's lexical diversity measure:** {herdan:.2f}"
    feedback += get_herdan_feedback(herdan)

    overall_score = get_lexical_richness_overall_score(cttr, yulek, simpsond, herdan)
    feedback += f"\n**Overall Score** {overall_score}/100"

    return feedback


def get_readability_feedback(text: str) -> str:
    feedback = "## 📘\u200b Readability Metrics\n\n"

    flesch_reading_ease = TextAnalyzer.get_flesch_reading_ease(text)
    feedback += f"**Flesch Reading Ease:** {flesch_reading_ease:.2f}"
    feedback += get_flesch_reading_ease_feedback(flesch_reading_ease)

    flesch_kincaid_grade = TextAnalyzer.get_flesch_kincaid_grade(text)
    feedback += f"**Flesch Kincaid Grade:** {flesch_kincaid_grade:.2f}"
    feedback += get_flesch_kincaid_grade_feedback(flesch_kincaid_grade)

    dale_chall_readability_score = TextAnalyzer.get_dale_chall_readability_score(text)
    feedback += f"**Dale Chall Readability Score:** {dale_chall_readability_score:.2f}"
    feedback += dale_chall_readability_score_feedback(dale_chall_readability_score)

    smog_index = TextAnalyzer.get_smog_index(text)
    feedback += f"**SMOG Index:** {smog_index:.2f}"
    feedback += get_smog_index_feedback(smog_index)

    overall_score = get_readibility_overall_score(
        flesch_kincaid_grade,
        smog_index,
    )
    feedback += "Based on your readability metrics, your presentation is understandable to " \
    f"listeners with about a **{round(overall_score)}th** grade education level."

    return feedback


def get_cttr_feedback(cttr: float) -> str:
    return get_feedback(
        cttr,
        LexRichCons.low_cttr_value,
        LexRichCons.high_cttr_value,
        LexRichCons.low_cttr,
        LexRichCons.medium_cttr,
        LexRichCons.high_cttr,
    )


def get_yulek_feedback(yulek: float) -> str:
    return get_feedback(
        yulek,
        LexRichCons.low_yulek_value,
        LexRichCons.high_yulek_value,
        LexRichCons.low_yulek,
        LexRichCons.medium_yulek,
        LexRichCons.high_yulek,
    )


def get_simpsond_feedback(simpsond: float) -> str:
    return get_feedback(
        simpsond,
        LexRichCons.low_simpsond_value,
        LexRichCons.high_simpsond_value,
        LexRichCons.low_simpsond,
        LexRichCons.medium_simpsond,
        LexRichCons.high_simpsond,
    )


def get_herdan_feedback(herdan: float) -> str:
    return get_feedback(
        herdan,
        LexRichCons.low_herdan_value,
        LexRichCons.high_herdan_value,
        LexRichCons.low_herdan,
        LexRichCons.medium_herdan,
        LexRichCons.high_herdan,
    )


def get_feedback(score: float,
                low_value: float,
                high_value: float,
                low_feedback: str,
                medium_feedback: str,
                high_feedback: str) -> str:
    feedback = ""

    if score < low_value:
        feedback = low_feedback
    elif score < high_value:
        feedback = medium_feedback
    else:
        feedback = high_feedback

    return feedback


def get_lexical_richness_overall_score(cttr: float,
                                       yulesk: float,
                                       simpsond: float,
                                       herdan: float) -> int:
    scores = [
        normalize_cttr(cttr),
        normalize_yulesk(yulesk),
        normalize_simpsond(simpsond),
        normalize_herdan(herdan),
    ]
    return round(sum(scores) / len(scores))


def normalize_cttr(value: float) -> float:
    return normalize_linear_relation(
        value,
        LexRichCons.low_cttr_value,
        LexRichCons.high_cttr_value,
    )


def normalize_yulesk(value: float) -> float:
    return normalize_inverse_relation(
        value,
        LexRichCons.low_yulek_value,
        LexRichCons.high_yulek_value,
    )


def normalize_simpsond(value: float) -> float:
    return normalize_inverse_relation(
        value,
        LexRichCons.low_simpsond_value,
        LexRichCons.high_simpsond_value,
    )


def normalize_herdan(value: float) -> float:
    return normalize_linear_relation(
        value,
        LexRichCons.low_herdan_value,
        LexRichCons.high_herdan_value,
    )


def normalize_linear_relation(value: float, low: float, high: float) -> float:
    return min(100, max(0, (value - low) / (high - low) * 100))


def normalize_inverse_relation(value: float, low: float, high: float) -> float:
    return min(100, max(0, (high - value) / (high - low) * 100))


def get_flesch_reading_ease_feedback(flesch_reading_ease: float) -> str:
    if flesch_reading_ease < ReadCons.very_low_flesch_reading_ease_value:
        return ReadCons.very_low_flesch_reading_ease
    if flesch_reading_ease < ReadCons.low_flesch_reading_ease_value:
        return ReadCons.low_flesch_reading_ease
    if flesch_reading_ease < ReadCons.medium_flesch_reading_ease_value:
        return ReadCons.medium_flesch_reading_ease
    if flesch_reading_ease < ReadCons.high_flesch_reading_ease_value:
        return ReadCons.high_flesch_reading_ease
    return ReadCons.very_high_flesch_reading_ease


def get_flesch_kincaid_grade_feedback(flesch_kincaid_grade: float) -> str:
    if flesch_kincaid_grade < ReadCons.very_low_flesch_kincaid_grade_value:
        return ReadCons.very_low_flesch_kincaid_grade
    if flesch_kincaid_grade < ReadCons.low_flesch_kincaid_grade_value:
        return ReadCons.low_flesch_kincaid_grade
    if flesch_kincaid_grade < ReadCons.medium_flesch_kincaid_grade_value:
        return ReadCons.medium_flesch_kincaid_grade
    return ReadCons.high_flesch_kincaid_grade


def dale_chall_readability_score_feedback(dale_chall_readability_score: float) -> str:
    return get_feedback(
       dale_chall_readability_score,
       ReadCons.low_dale_chall_readability_score_value,
       ReadCons.high_dale_chall_readability_score_value,
       ReadCons.low_dale_chall_readability_score,
       ReadCons.medium_dale_chall_readability_score,
       ReadCons.high_dale_chall_readability_score,
   )


def get_smog_index_feedback(smog_index: float) -> str:
    if smog_index < ReadCons.low_smog_index_value:
        return ReadCons.low_smog_index
    if smog_index < ReadCons.medium_smog_index_value:
        return ReadCons.medium_smog_index
    if smog_index < ReadCons.high_smog_index_value:
        return ReadCons.high_smog_index
    return ReadCons.very_high_smog_index


def get_readibility_overall_score(flesch_kincaid_grade: float,
                                  smog_index: float) -> float:

    return (flesch_kincaid_grade + smog_index) / 2
