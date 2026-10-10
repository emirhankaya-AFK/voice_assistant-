[English](README.md) | [Türkçe](README_TR.md) | [Deutsch](README_DE.md)

## English
### Purpose
An interactive assistant that records microphone input, sends the audio to Gemini for multimodal analysis, converts the answer to Turkish speech, and plays it through the system audio output.

### Verified Features
- Asynchronous microphone recording (`audio_recorder.py`)
- Gemini audio client for multimodal analysis (`gemini_voice.py`)
- Text-to-speech generation and playback (`tts_player.py`)
- Interactive loop in `main.py`
- Configuration template (`config.example.json`)

### Stack
- Python 3
- Dependencies: sounddevice, soundfile, gtts, requests, numpy, cffi
- Linux playback via VLC (command-line player)

### Setup
```bash
pip install sounddevice soundfile gtts requests numpy cffi
sudo apt-get install vlc   # Linux only
```
Copy `config.example.json` to `config.json`, insert your Gemini API key, and keep the file private.

### Usage
```bash
python main.py
```
Press **Enter** to start recording a question, speak, then press **Enter** again to stop. Type `q` and press Enter to exit.

### Limitations
- Requires a valid Gemini API key.
- Playback relies on VLC on Linux; other platforms may need alternative players.
- Speech output is currently limited to Turkish.

## Türkçe
### Amaç
Mikrofon girişi kaydedilen, Gemini tarafından multimodal analiz için gönderilen, cevabın Türkçe konuşmaya dönüştürülüp sistem ses çıkarıyla çalan etkileşimli bir asistan.

### Doğrulanan Özellikler
- Asenkron mikrofon kaydı (`audio_recorder.py`)
- Gemini ses istemcisi multimodal analiz için (`gemini_voice.py`)
- Metin‑ses üretimi ve oynatma (`tts_player.py`)
- `main.py` içindeki etkileşimli döngü
- Yapılandırma şablonu (`config.example.json`)

### Yığın
- Python 3
- Bağımlılıklar: sounddevice, soundfile, gtts, requests, numpy, cffi
- Linux'ta VLC komut satırı oynatıcısı ile ses çıkışı

### Kurulum
```bash
pip install sounddevice soundfile gtts requests numpy cffi
sudo apt-get install vlc   # sadece Linux
```
`config.example.json` dosyasını `config.json` olarak kopyalayın, Gemini API anahtarınızı ekleyin ve dosyayı gizli tutun.

### Kullanım
```bash
python main.py
```
Bir soru kaydetmek için **Enter** tuşuna basın, konuşun, ardından kaydı durdurmak için tekrar **Enter** basın. Çıkmak için `q` yazıp Enter'a basın.

### Sınırlamalar
- Geçerli bir Gemini API anahtarı gereklidir.
- Oynatma Linux'ta VLC'ye bağımlıdır; diğer platformlar farklı bir oynatıcı gerektirebilir.
- Ses çıktısı şu anda sadece Türkçe olarak üretilir.

## Deutsch
### Zweck
Ein interaktiver Assistent, der Mikrofoneingabe aufnimmt, das Audio an Gemini für multimodale Analyse sendet, die Antwort in türkische Sprache umwandelt und sie über die Systemaudioausgabe abspielt.

### Verifizierte Funktionen
- Asynchrone Mikrofonaufnahme (`audio_recorder.py`)
- Gemini Audio‑Client für multimodale Analyse (`gemini_voice.py`)
- Text‑zu‑Sprache‑Generierung und Wiedergabe (`tts_player.py`)
- Interaktive Schleife in `main.py`
- Konfigurationsvorlage (`config.example.json`)

### Technologie‑Stack
- Python 3
- Abhängigkeiten: sounddevice, soundfile, gtts, requests, numpy, cffi
- Linux‑Wiedergabe über VLC (Befehlszeilen‑Player)

### Einrichtung
```bash
pip install sounddevice soundfile gtts requests numpy cffi
sudo apt-get install vlc   # nur Linux
```
Kopiere `config.example.json` nach `config.json`, füge deinen Gemini‑API‑Schlüssel ein und halte die Datei privat.

### Verwendung
```bash
python main.py
```
Drücke **Enter**, um eine Frage aufzunehmen, spreche, dann erneut **Enter**, um die Aufnahme zu beenden. Gebe `q` ein und drücke Enter, um das Programm zu beenden.

### Einschränkungen
- Erfordert einen gültigen Gemini‑API‑Schlüssel.
- Die Wiedergabe setzt VLC unter Linux voraus; auf anderen Plattformen kann ein anderer Player nötig sein.
- Die Sprachausgabe ist derzeit auf Türkisch beschränkt.
