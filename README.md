# Voice-to-Voice Personal AI Assistant

[English](README.md) | [Türkçe](README_TR.md)

An interactive assistant that records microphone input, sends the audio to Gemini for multimodal analysis, converts the answer to Turkish speech, and plays it through the system audio output.

## Components

- `main.py`: interactive assistant loop
- `audio_recorder.py`: asynchronous microphone recording
- `gemini_voice.py`: Gemini audio client
- `tts_player.py`: text-to-speech generation and playback
- `config.example.json`: safe configuration template

## Setup

```bash
pip install sounddevice soundfile gtts requests numpy cffi
```

Linux playback uses VLC's command-line player:

```bash
sudo apt-get install vlc
```

Copy `config.example.json` to `config.json`, add your Gemini API key, and keep that file private.

## Run

```bash
python main.py
```

Press `Enter` to record a question and enter `q` to exit.

