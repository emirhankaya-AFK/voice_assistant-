import subprocess
import os

class AudioRecorder:
    def __init__(self, sample_rate=16000):
        self.sample_rate = sample_rate

    def record_audio(self, file_path, duration=5):
        """
        Records audio from the microphone using the native Linux 'arecord' utility.
        This avoids PortAudio/sounddevice compilation issues on Linux.
        """
        print(f"\n🎙️  Sesiniz kaydediliyor ({duration} saniye)... Konuşun...")
        
        # Command: arecord -d <duration> -f S16_LE -r <sample_rate> -t wav <file_path>
        cmd = [
            "arecord",
            "-d", str(duration),
            "-f", "S16_LE",
            "-r", str(self.sample_rate),
            "-t", "wav",
            file_path
        ]
        
        try:
            # Run arecord, redirecting stderr to DEVNULL to keep console clean
            result = subprocess.run(
                cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=duration + 3
            )
            
            if result.returncode == 0 and os.path.exists(file_path):
                print("🛑 Kayıt tamamlandı. İşleniyor...")
                return True
            else:
                print("[ERROR] arecord kayıt alamadı (Cihaz meşgul veya mikrofon bulunamadı).")
                return False
        except subprocess.TimeoutExpired:
            print("[WARN] Ses kaydı zaman aşımına uğradı.")
            return False
        except Exception as e:
            print(f"[ERROR] Ses kaydı sırasında sistem hatası: {e}")
            return False
