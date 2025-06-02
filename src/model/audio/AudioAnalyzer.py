from operator import itemgetter

import librosa
import numpy as np


def get_rms(audio_path: str) -> np.ndarray:
    y, _ = librosa.load(audio_path)
    return librosa.feature.rms(y=y)[0]


def get_snr(rms: np.ndarray) -> float:
    noise_threshold = np.percentile(rms, 10)
    speech_energy = np.mean(rms[rms > noise_threshold])
    noise_energy = np.mean(rms[rms <= noise_threshold])

    return 10 * np.log10(speech_energy / noise_energy)


def get_speaking_rate(chunks: list, length: int, interval: int = 5) -> dict:
    rates = {}

    for i in range(0, length, interval):
        count = sum(
            i < chunk["timestamp"][1] < i + interval
            for chunk in chunks
        )
        rates[i] = (count / interval) * 60

    return dict(sorted(rates.items(), key=itemgetter(0)))
