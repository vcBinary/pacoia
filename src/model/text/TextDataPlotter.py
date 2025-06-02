import pandas as pd


def get_words_distribution_plot(word_frequencies: dict[str, int]) -> pd.DataFrame:
    return pd.DataFrame({
        "Word": list(word_frequencies.keys()),
        "Appearances": list(word_frequencies.values()),
    })
