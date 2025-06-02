from typing import Callable, Union

import gradio as gr
import pandas as pd


class Interface:
    def __init__(self, function_ptr: Callable[[str, list[str]], list[Union[str, pd.DataFrame]]]) -> None:
        title = "PACOIA: Plataforma Automatizada para la evaluación de Comunicación Oral en Inglés Académico"
        css = "footer{display:none !important}"

        with gr.Blocks(title=title, css=css) as self.blocks:
            with gr.Row():
                gr.Markdown("# 📄 Plataforma Automatizada para la evaluación de Comunicación Oral en Inglés Académico")
            with gr.Row():
                audio_box = gr.Audio(type="filepath")
            with gr.Row():
                checkbox_group = gr.CheckboxGroup(
                    choices=[
                        "Introduction",
                        "Background",
                        "Innovation",
                        "Description",
                        "Organization",
                        "Language",
                    ],
                    label="Choose the parts to be graded",
                )
            with gr.Row():
                submit_btn = gr.Button("Submit", variant="primary")

            with gr.Tab("Transcription"):
                with gr.Row():
                    transcription = gr.Textbox(label="Transcription")

            with gr.Tab("Words Distribution"):
                with gr.Row():
                    words_distribution_plot = gr.BarPlot(
                        label="Words Distribution",
                        x="Word",
                        y="Appearances",
                        title="Words Distribution",
                        x_title="Words",
                        y_title="Appearances",
                        x_axis_labels_visible=False,
                    )
                with gr.Row():
                    words_distribution_feedback = gr.Markdown(label="Words Distribution Feedback", line_breaks=True)

            with gr.Tab("Lexical Richness"):
                with gr.Row():
                    lexical_richness_feedback = gr.Markdown(label="Frequencies feedback", line_breaks=True)

            with gr.Tab("Readability"):
                with gr.Row():
                    readability_feedback = gr.Markdown(label="Frequencies feedback", line_breaks=True)

            with gr.Tab("Acoustic metrics"):
                with gr.Row():
                    with gr.Row():
                        speaking_rate_plot = gr.LinePlot(
                            x="Time (s)",
                            y="Words per minute",
                            title="Speaking rate Over Time",
                            x_title="Time (s)",
                            y_title="Words per minute",
                            label="Speaking Rate Plot",
                        )
                with gr.Row():
                    speaking_rate_feedback = gr.Markdown(label="Speaking rate feedback", line_breaks=True)

                with gr.Row():
                    rms_plot = gr.LinePlot(
                        x="Time (s)",
                        y="RMS Energy",
                        title="RMS Energy Over Time",
                        x_title="Time (s)",
                        y_title="RMS Energy",
                        label="RMS Energy Plot",
                    )
                with gr.Row():
                    rms_feedback = gr.Markdown(label="RMS feedback", line_breaks=True)

                with gr.Row():
                    snr_plot = gr.LinePlot(
                        x="Time (s)",
                        y="SNR Over Time",
                        title="SNR Over Time",
                        x_title="Time (s)",
                        y_title="SNR",
                        label="SNR Plot",
                    )
                with gr.Row():
                    snr_feedback = gr.Markdown(label="SNR feedback")

            with gr.Tab("LLM feedback"):
                with gr.Row():
                    introduction_feedback = gr.Markdown(label="Introduction feedback")
                with gr.Row():
                    background_feedback = gr.Markdown(label="Background feedback")
                with gr.Row():
                    innovation_feedback = gr.Markdown(label="Innovation feedback")
                with gr.Row():
                    description_feedback = gr.Markdown(label="Description feedback")
                with gr.Row():
                    organization_feedback = gr.Markdown(label="Organization feedback")
                with gr.Row():
                    language_feedback = gr.Markdown(label="Language feedback")

            submit_btn.click(
                fn=function_ptr,
                inputs=[audio_box, checkbox_group],
                outputs=[
                    transcription,
                    words_distribution_plot,
                    words_distribution_feedback,
                    lexical_richness_feedback,
                    readability_feedback,
                    speaking_rate_plot,
                    speaking_rate_feedback,
                    rms_plot,
                    rms_feedback,
                    snr_plot,
                    snr_feedback,
                    introduction_feedback,
                    background_feedback,
                    innovation_feedback,
                    description_feedback,
                    organization_feedback,
                    language_feedback,
                ],
            )
