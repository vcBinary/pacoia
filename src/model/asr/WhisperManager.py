import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline


class WhisperManager:
    def __init__(self, torch_dtype: torch.dtype, device: str) -> None:
        self.model_id = "openai/whisper-small"
        model = AutoModelForSpeechSeq2Seq.from_pretrained(
            self.model_id,
            torch_dtype=torch_dtype,
            low_cpu_mem_usage=True,
            use_safetensors=True,
        )

        model.to(device)
        model = torch.compile(model)
        processor = AutoProcessor.from_pretrained(self.model_id)
        forced_language = ("<|en|>")
        generate_kwargs = {"language": forced_language}

        self.pipeline = pipeline(
            "automatic-speech-recognition",
            model=model,
            tokenizer=processor.tokenizer,
            feature_extractor=processor.feature_extractor,
            torch_dtype=torch_dtype,
            device=device,
            return_timestamps=True,
            generate_kwargs=generate_kwargs,
        )

    def transcribe(self, audio_path: str) -> dict:
        return self.pipeline(audio_path)
