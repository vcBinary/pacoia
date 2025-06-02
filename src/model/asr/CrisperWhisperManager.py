import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline


class CrisperWhisperManager:
    def __init__(self, torch_dtype: torch.dtype, device: str) -> None:
        self.model_id = "nyrahealth/CrisperWhisper"
        model = AutoModelForSpeechSeq2Seq.from_pretrained(
            self.model_id,
            torch_dtype=torch_dtype,
            low_cpu_mem_usage=True,
            use_safetensors=True,
            use_cache=False,
        )

        model.to(device)
        model = torch.compile(model)
        processor = AutoProcessor.from_pretrained(self.model_id)
        forced_language = ("<|en|>")
        generate_kwargs = {"language": forced_language, "num_beams": 1}

        self.pipeline = pipeline(
            "automatic-speech-recognition",
            model=model,
            tokenizer=processor.tokenizer,
            feature_extractor=processor.feature_extractor,
            chunk_length_s=90,
            batch_size=1,
            torch_dtype=torch_dtype,
            device=device,
            return_timestamps="word",
            generate_kwargs=generate_kwargs,
        )

    def transcribe(self, audio_path: str) -> dict:
        return self.pipeline(audio_path)
