import os
import json
import sys
from audio_recorder import AudioRecorder
from gemini_voice import GeminiVoiceClient
from tts_player import TTSPlayer

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")
TEMP_INPUT_PATH = os.path.join(os.path.dirname(__file__), "temp_input.wav")

def load_config():
    if not os.path.exists(CONFIG_PATH):
        print(f"[ERROR] Config dosyası bulunamadı: {CONFIG_PATH}")
        return {}
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def main():
    print("====================================================")
    print("🎙️  Sesli Kişisel Yapay Zeka Asistanı Başlatılıyor...  🎙️")
    print("====================================================")
    
    config = load_config()
    if not config:
        return
        
    api_key = config.get("gemini_api_key", "")
    sample_rate = config.get("sample_rate", 16000)
    duration = config.get("record_duration", 5)
    
    # Initialize components
    recorder = AudioRecorder(sample_rate=sample_rate)
    voice_client = GeminiVoiceClient(api_key=api_key)
    player = TTSPlayer()
    
    if not voice_client.enabled:
        print("\n[WARN] Yapay Zekayı sesli kullanabilmek için 'config.json' dosyasına")
        print("geçerli bir 'gemini_api_key' girmelisiniz.")
        
    print("\nKomutlar:")
    print(" -> Konuşmayı başlatmak için [ENTER] tuşuna basın.")
    print(" -> Çıkış yapmak için 'q' yazıp [ENTER] tuşuna basın.\n")
    
    # Welcome greeting
    if voice_client.enabled:
        player.speak("Merhaba! Ben senin sesli asistanınım. Konuşmak için hazır olduğunda giriş tuşuna basabilirsin.")
        
    while True:
        try:
            cmd = input("\n[ENTER - Konuş] / [q - Çıkış] > ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n[INFO] Çıkış yapılıyor...")
            break
            
        if cmd.lower() == 'q':
            print("[INFO] Asistan kapatıldı. Görüşmek üzere!")
            if voice_client.enabled:
                player.speak("Görüşmek üzere, kendine iyi bak!")
            break
            
        # Record audio
        success = recorder.record_audio(TEMP_INPUT_PATH, duration=duration)
        if not success:
            continue
            
        # Send to Gemini and get text answer
        print("🧠  Yapay zeka sesi analiz ediyor...")
        ai_response = voice_client.send_audio(TEMP_INPUT_PATH)
        
        # Clean up input audio
        if os.path.exists(TEMP_INPUT_PATH):
            os.remove(TEMP_INPUT_PATH)
            
        # Play back the answer
        if ai_response:
            player.speak(ai_response)
        else:
            print("[WARN] Yapay zekadan yanıt alınamadı.")

if __name__ == "__main__":
    main()
