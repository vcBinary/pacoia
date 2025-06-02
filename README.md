# PACOIA project
![CI](https://github.com/vcbinary/pacoia/actions/workflows/CI.yml/badge.svg)

Plataforma Automatizada para la evaluación de Comunicación Oral en Inglés Académico

## Requirements
- [Python 3.12](https://www.python.org/)
- [Astral uv](https://docs.astral.sh/uv/)
- [FFmpeg](https://www.ffmpeg.org/)
  
## Installation

### Using Virtualenv
```bash
uv sync --locked --all-extras --dev
```

## Usage
```bash
uv run -m src.main --model <model>
```

Currently the only supported ASR models are `CrisperWhisper` and `Whisper`

> [!NOTE]  
> In order to use CrisperWhisper you must generate a token [here](https://huggingface.co/nyrahealth/CrisperWhisper) and assign it to the environmental variable `HF_TOKEN`, where the token will be read by the application

Then the application will be deployed in `http://127.0.0.1:7860`
