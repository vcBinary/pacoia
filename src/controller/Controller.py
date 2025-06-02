from typing import Union

import pandas as pd

from src.model.asr.CrisperWhisperManager import CrisperWhisperManager
from src.model.asr.WhisperManager import WhisperManager
from src.model.audio import AudioAnalyzer, AudioDataPlotter, AudioFeedback
from src.model.llm.LLMPeer import LLMPeer
from src.model.text import TextAnalyzer, TextDataPlotter, TextFeedback
from src.utils import Utils


class Controller:
    def __init__(self, model: str, llm_peer: LLMPeer) -> None:
        Utils.login_hf()
        device = Utils.default_device()
        torch_dtype = Utils.default_dtype()
        self.model = model
        self.llm_peer = llm_peer

        if model == "CrisperWhisper":
            self.asr_manager: Union[WhisperManager, CrisperWhisperManager] = \
                CrisperWhisperManager(torch_dtype, device)
        else:
            self.asr_manager = WhisperManager(torch_dtype, device)

    def generate_outputs_whisper(self, audio_path: str, options: list[str]) -> list[Union[str, pd.DataFrame]]:
        speech_data = self.asr_manager.transcribe(audio_path)
        word_frequencies = TextAnalyzer.get_words_distribution(speech_data["text"])
        rms = AudioAnalyzer.get_rms(audio_path)
        mean_snr = AudioAnalyzer.get_snr(rms)

        output = []
        output.append(speech_data["text"])
        output.append(TextDataPlotter.get_words_distribution_plot(word_frequencies))
        output.append(TextFeedback.get_words_distribution_feedback(word_frequencies))

        output.append(TextFeedback.get_lexical_richness_feedback(speech_data["text"]))
        output.append(TextFeedback.get_readability_feedback(speech_data["text"]))

        output.append(AudioDataPlotter.get_rms_plot(rms))
        output.append(AudioFeedback.get_rms_feedback(rms))

        output.append(AudioDataPlotter.get_snr_plot(rms))
        output.append(AudioFeedback.get_snr_feedback(mean_snr))

        punctuated_transcription = self.llm_peer.get_punctuated_transcription(speech_data["text"])

        if "Introduction" in options:
            output.append(self.llm_peer.get_introduction_evaluation(punctuated_transcription))
        else:
            output.append("")

        if "Background" in options:
            output.append(self.llm_peer.get_background_evaluation(punctuated_transcription))
        else:
            output.append("")

        if "Innovation" in options:
            output.append(self.llm_peer.get_innovation_evaluation(punctuated_transcription))
        else:
            output.append("")

        if "Description" in options:
            output.append(self.llm_peer.get_description_evaluation(punctuated_transcription))
        else:
            output.append("")

        if "Organization" in options:
            output.append(self.llm_peer.get_organization_evaluation(punctuated_transcription))
        else:
            output.append("")

        if "Language" in options:
            output.append(self.llm_peer.get_language_evaluation(punctuated_transcription))
        else:
            output.append("")

        return output

    def generate_outputs_crisper_whisper(self, audio_path: str, options: list[str]) -> list[Union[str, pd.DataFrame]]:
        speech_data = self.asr_manager.transcribe(audio_path)
        word_frequencies = TextAnalyzer.get_words_distribution(speech_data["text"])
        rms = AudioAnalyzer.get_rms(audio_path)
        mean_snr = AudioAnalyzer.get_snr(rms)
        word_count = len(word_frequencies)
        last_chunk_timestamp = speech_data["chunks"][len(speech_data["chunks"]) - 1]["timestamp"]
        
        if not last_chunk_timestamp[1]:
            speech_data["chunks"][len(speech_data["chunks"]) - 1]["timestamp"] = \
                (last_chunk_timestamp[0], last_chunk_timestamp[0])
            
        length = speech_data["chunks"][len(speech_data["chunks"]) - 1]["timestamp"][1]
        rates = AudioAnalyzer.get_speaking_rate(speech_data["chunks"], length)

        output = []
        output.append(speech_data["text"])
        output.append(TextDataPlotter.get_words_distribution_plot(word_frequencies))
        output.append(TextFeedback.get_words_distribution_feedback(word_frequencies))

        output.append(TextFeedback.get_lexical_richness_feedback(speech_data["text"]))
        output.append(TextFeedback.get_readability_feedback(speech_data["text"]))

        output.append(AudioDataPlotter.get_speaking_rate_plot(rates))
        output.append(AudioFeedback.get_speaking_rate_feedback(word_count, length))

        output.append(AudioDataPlotter.get_rms_plot(rms))
        output.append(AudioFeedback.get_rms_feedback(rms))

        output.append(AudioDataPlotter.get_snr_plot(rms))
        output.append(AudioFeedback.get_snr_feedback(mean_snr))

        punctuated_transcription = self.llm_peer.get_punctuated_transcription(speech_data["text"])

        if "Introduction" in options:
            output.append(self.llm_peer.get_introduction_evaluation(punctuated_transcription))
        else:
            output.append("")

        if "Background" in options:
            output.append(self.llm_peer.get_background_evaluation(punctuated_transcription))
        else:
            output.append("")

        if "Innovation" in options:
            output.append(self.llm_peer.get_innovation_evaluation(punctuated_transcription))
        else:
            output.append("")

        if "Description" in options:
            output.append(self.llm_peer.get_description_evaluation(punctuated_transcription))
        else:
            output.append("")

        if "Organization" in options:
            output.append(self.llm_peer.get_organization_evaluation(punctuated_transcription))
        else:
            output.append("")

        if "Language" in options:
            output.append(self.llm_peer.get_language_evaluation(punctuated_transcription))
        else:
            output.append("")

        return output
