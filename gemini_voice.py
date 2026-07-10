import base64
import requests
import json
import os

class GeminiVoiceClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.enabled = True
        
        if not api_key or "YOUR_GEMINI" in api_key:
            print("[WARN] Gemini API Anahtarı bulunamadı veya varsayılan değerde bırakılmış. Asistan yanıt veremez.")
            self.enabled = False

    def send_audio(self, audio_path):
        """
        Sends the WAV audio file at audio_path directly to Gemini API.
        Returns the text response from the model.
        """
        if not self.enabled:
            return "Gemini API anahtarı tanımlanmadığı için sesinizi işleyemiyorum."
            
        if not os.path.exists(audio_path):
            return "Ses kayıt dosyası bulunamadı."

        try:
            # 1. Base64 encode the audio file
            with open(audio_path, "rb") as f:
                audio_data = f.read()
                base64_audio = base64.b64encode(audio_data).decode("utf-8")
                
            # 2. Format the API payload
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={self.api_key}"
            headers = {
                "Content-Type": "application/json"
            }
            
            # Prompts optimized for Voice-to-Voice responses
            system_instruction = (
                "Sen kullanıcının sesli olarak konuştuğu kişisel bir yapay zeka asistanısın. "
                "Kullanıcının gönderdiği ses kaydını dinle ve ona samimi, kısa ve sohbet dilinde Türkçe cevap ver. "
                "Cevaplarında kesinlikle Markdown biçimlendirmeleri (örneğin **, *, #) veya kod blokları kullanma. "
                "Metin doğrudan seslendirileceği (TTS) için kelimeleri okunduğu gibi düz metin halinde yaz."
            )
            
            payload = {
                "contents": [{
                    "parts": [
                        {
                            "inline_data": {
                                "mime_type": "audio/wav",
                                "data": base64_audio
                            }
                        },
                        {
                            "text": system_instruction
                        }
                    ]
                }]
            }
            
            # 3. Call the API
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                answer = data['candidates'][0]['content']['parts'][0]['text']
                return answer.strip()
            else:
                print(f"[ERROR] Gemini API Hatası. Durum: {response.status_code}, Yanıt: {response.text}")
                return "Gemini API ses kaydınızı işlerken bir hata döndürdü."
                
        except Exception as e:
            print(f"[ERROR] Gemini API bağlantı hatası: {e}")
            return "API sunucusuna bağlanırken bir bağlantı hatası oluştu."
