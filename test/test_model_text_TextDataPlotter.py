import src.model.text.TextDataPlotter as TextDataPlotter
import src.model.text.TextAnalyzer as TextAnalyzer
import pandas as pd

class TestTextDataPlotter:

    def test_get_rms_plot(self):
        frequencies = TextAnalyzer.get_words_distribution("hola")
        assert type(TextDataPlotter.get_words_distribution_plot(frequencies)) == pd.DataFrame