import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

duration = 10  # Kaydın süresi (saniye)
sample_rate = 44100  # Örnekleme hızı (Hz)
filename = 'recording.wav'


def record_audio(duration, sample_rate=44100):
    print("recording")
    audio_data = sd.rec(int(duration * sample_rate),samplerate=sample_rate, channels=1,dtype='int16')
    sd.wait()
    print("recording complate")
    return  audio_data

def play_audio(audio_data, sample_rate=44100):
    print("recording play")
    sd.play(audio_data,samplerate=sample_rate)
    sd.wait()
    print("playing complate")

def save_record(filename,audio_data,sample_rate):
    print(f"dosyaya kayıt ediliyor{ filename}")
    wav.write(filename,sample_rate,audio_data)
    print("kayıt tamam")

# Ses kaydını yap
audio_data = record_audio(duration, sample_rate)

# Kaydedilen sesi çal
play_audio(audio_data, sample_rate)

save_record(filename,audio_data,sample_rate)