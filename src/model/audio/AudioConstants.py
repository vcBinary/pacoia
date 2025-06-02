# RMS Constants

low_mean_rms_value = 0.05
normal_mean_rms_value = 0.2

low_mean_rms = \
"""🔴 Low mean RMS (soft speech, whispers): 0.01 - 0.05 \
Your speech is quite soft or whispered. Consider speaking a \
bit louder to improve clarity, especially in environments \
with background noise.
"""

normal_mean_rms = \
"""🟢\u200b Normal mean RMS (conversational speech): 0.05 - 0.2 \
"Your speech is at a normal, conversational volume. This range is \
"ideal for clear communication in most environments.
"""

high_mean_rms = \
"""🟠 High mean RMS (loud speech, shouting): 0.2 - 0.5+ \
Your speech is loud or even close to shouting. Try to lower the \
volume slightly to avoid straining your voice or overwhelming \
the listener.
"""

# SNR Constants

very_low_mean_snr_value = 5
low_mean_snr_value = 10
normal_mean_snr_value = 15
high_mean_snr_value = 20

very_low_mean_snr = \
"""🔴 The audio is very hard to hear due to excessive background \
noise. Speech is unclear, and it may be challenging to understand the \
content. Significant improvements are needed for clarity.
"""

low_mean_snr = \
"""🟠 The audio quality is poor, with noticeable background noise. \
While speech is still somewhat audible, the overall clarity is \
affected, making it harder to follow the conversation.
"""

normal_mean_snr = \
"""🟢\u200b The audio is fairly clear, but there's noticeable background \
noise. While the speech is still understandable, the quality can be \
improved for a better listening experience.
"""

high_mean_snr = \
"""🟠 The speech is clear and easy to understand, though there might \
be slight background noise. Overall, it's good quality for most uses, \
though a little enhancement could make it perfect.
"""

very_high_snr = \
"""🔴 The audio is very clear with no noticeable background noise. \
Speech is easily understandable, and the quality is ideal for \
communication or professional use.
"""

# Speaking Rate Constants

very_slow_speaking_rate_value = 70
slow_speaking_rate_value = 110
normal_speaking_rate_value = 150
fast_speaking_rate_value = 190

very_slow_speaking_rate = \
"""🔴 Your speaking rate is quite slow, which may make the speech feel \
overly drawn out. Consider increasing your pace slightly to maintain \
engagement and improve fluidity.
"""

slow_speaking_rate = \
"""🟠 Your speech is on the slower side, which could be beneficial for \
clarity but might feel a bit sluggish. Consider speeding up a little to \
maintain a more natural rhythm.
"""

normal_speaking_rate = \
"""🟢\u200b Your speaking rate is within the normal range, making your speech \
clear and easy to follow. This is ideal for most conversational \
and presentation settings.
"""

fast_speaking_rate = \
"""🟠 You're speaking at a fast pace. While this shows enthusiasm, \
it could make it harder for listeners to catch every word. Try slowing \
down slightly to improve clarity.
"""

very_fast_speaking_rate = \
"""🔴 Your speaking rate is very fast, which might be overwhelming for \
some listeners. Consider pausing occasionally to allow your audience to \
absorb the information.
"""
