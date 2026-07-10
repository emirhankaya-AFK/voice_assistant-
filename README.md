# Sesli Kişisel Yapay Zeka Asistanı (Voice-to-Voice AI Assistant)

Bu proje, bilgisayarınızın mikrofonunu kullanarak ses kaydı alan, bu kaydı doğrudan çok modlu (multimodal) Gemini API'sine gönderip analiz eden ve gelen yapay zeka cevabını Türkçe seslendirmeye (Text-to-Speech) dönüştürerek hoparlörden çalan interaktif bir sesli asistandır.

## Proje Yapısı

*   `main.py`: Asistan döngüsünü kontrol eden ve interaktif komut satırı arayüzünü sağlayan ana dosyadır.
*   `audio_recorder.py`: `sounddevice` ve `soundfile` kütüphanelerini kullanarak mikrofon girişinden asenkron ses kaydı alan modüldür.
*   `gemini_voice.py`: Kaydedilen ses dosyasını Base64 formatına çevirip doğrudan Gemini API'sine (multimodal ses algılama yeteneği ile) gönderen istemci modülüdür.
*   `tts_player.py`: Yapay zekanın ürettiği metin yanıtını `gTTS` ile Türkçe ses dosyasına çeviren ve sistemdeki VLC (`cvlc`) veya diğer ses çalarlarla oynatan modüldür.
*   `config.json`: Gemini API anahtarını ve ses kayıt parametrelerini barındırır.

## Kurulum ve Bağımlılıklar

Gerekli olan Python kütüphanelerini kurun:

```bash
pip install sounddevice soundfile gtts requests numpy cffi
```

### Sistem Ses Çalar Gereksinimi (Linux)
Yazılan kod, ses dosyasını oynatmak için Linux üzerindeki en popüler oynatıcılardan biri olan **VLC**'nin terminal modunu (`cvlc`) kullanır. Eğer bilgisayarınızda VLC kurulu değilse:

```bash
sudo apt-get install vlc
```

---

## Gemini API Anahtarı Alma

Sistemin yapay zeka cevapları üretebilmesi için ücretsiz bir Gemini API anahtarı almanız gerekir:
1.  [Google AI Studio](https://aistudio.google.com/) adresine gidin.
2.  Google hesabınızla giriş yapın.
3.  **Get API Key** butonuna tıklayarak yeni bir anahtar oluşturun.
4.  Oluşturduğunuz anahtarı kopyalayıp projedeki `config.json` dosyasında yer alan `"gemini_api_key"` değerine yapıştırın.

## Nasıl Çalıştırılır?

Projeyi başlatmak için dizin içerisinden `main.py` dosyasını çalıştırın:

```bash
python main.py
```

### Kullanım Kılavuzu:
1.  Uygulama başladığında size sesli bir selamlama yapacaktır.
2.  Soru sormak/konuşmak istediğinizde **`ENTER`** tuşuna basın.
3.  Ekranda `Sesiniz kaydediliyor...` yazısı göründüğünde mikrofona konuşun (varsayılan kayıt süresi 5 saniyedir).
4.  Kayıt bittiğinde yapay zeka sesinizi analiz edecek ve hoparlörden sesli olarak yanıt verecektir.
5.  Uygulamadan çıkmak için **`q`** yazıp ENTER tuşuna basmanız yeterlidir.
