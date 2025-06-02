from numpy import mean, ndarray

from src.model.audio import AudioConstants


def get_rms_feedback(rms: ndarray) -> str:
    mean_rms = mean(rms)

    if mean_rms < AudioConstants.low_mean_rms_value:
        return AudioConstants.low_mean_rms
    if mean_rms > AudioConstants.normal_mean_rms_value:
        return AudioConstants.high_mean_rms

    return AudioConstants.normal_mean_rms


def get_snr_feedback(mean_snr: float) -> str:
    if mean_snr < AudioConstants.very_low_mean_snr_value:
        return AudioConstants.very_low_mean_snr
    if mean_snr < AudioConstants.low_mean_snr_value:
        return AudioConstants.low_mean_snr
    if mean_snr < AudioConstants.normal_mean_snr_value:
        return AudioConstants.normal_mean_snr
    if mean_snr < AudioConstants.high_mean_snr_value:
        return AudioConstants.high_mean_snr

    return AudioConstants.very_high_snr


def get_speaking_rate_feedback(word_count: int, length: int) -> str:
    mean_rate = word_count / length

    if mean_rate < AudioConstants.very_slow_speaking_rate_value:
        return AudioConstants.very_slow_speaking_rate
    if mean_rate < AudioConstants.slow_speaking_rate_value:
        return AudioConstants.slow_speaking_rate
    if mean_rate < AudioConstants.normal_speaking_rate_value:
        return AudioConstants.normal_speaking_rate
    if mean_rate < AudioConstants.fast_speaking_rate_value:
        return AudioConstants.fast_speaking_rate

    return AudioConstants.very_fast_speaking_rate
