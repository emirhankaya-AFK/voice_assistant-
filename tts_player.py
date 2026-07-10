import os
import subprocess
from gtts import gTTS

class TTSPlayer:
    def __init__(self, lang='tr'):
        self.lang = lang

    def speak(self, text, output_path="temp_response.mp3"):
        """
        Converts text to speech using gTTS and plays it back using cvlc or other players.
        """
        if not text:
            return False
            
        print(f"🤖  AI: {text}")
        
        try:
            # 1. Generate MP3 file using gTTS
            tts = gTTS(text=text, lang=self.lang)
            tts.save(output_path)
            
            # 2. Play the MP3 file using system players
            # We prioritize cvlc (VLC Headless) and fallback to other options
            played = False
            players = [
                ["cvlc", "--play-and-exit", output_path],
                ["vlc", "--play-and-exit", output_path],
                ["paplay", output_path], # PulseAudio player
                ["play", output_path]     # SoX player
            ]
            
            for cmd in players:
                try:
                    # Run the command and direct outputs to DEVNULL to keep console clean
                    result = subprocess.run(
                        cmd,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                        timeout=15
                    )
                    if result.returncode == 0:
                        played = True
                        break
                except (FileNotFoundError, subprocess.TimeoutExpired):
                    continue
            
            if not played:
                print("[WARN] Sistemde uygun ses çalar (cvlc, vlc, paplay) bulunamadı. Ses oynatılamadı.")
                
            # 3. Clean up the temporary MP3 file
            if os.path.exists(output_path):
                os.remove(output_path)
                
            return played
            
        except Exception as e:
            print(f"[ERROR] Ses sentezleme veya oynatma hatası: {e}")
            return False
