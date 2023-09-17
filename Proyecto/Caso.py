import librosa
import numpy as np
import matplotlib.pyplot as plt

def detect_alarm(audio_file):
    # Cargar el archivo de audio
    audio_data, sample_rate = librosa.load(audio_file, sr=None)

    # Realizar un análisis de características
    spectrogram = np.abs(librosa.stft(audio_data))

    threshold = 0.5  

    # Calcular la energia promedio en el espectrograma
    energy = np.mean(spectrogram)

    # Realizar la detección de alarma basada en el umbral
    if energy > threshold:
        print("Alarma Detectada")
    else:
        print("El audio no contiene una alarma")

    
      # Desplegar el espectrograma
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(librosa.amplitude_to_db(spectrogram, ref=np.max), y_axis='log', x_axis='time')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Espectrograma')
    plt.show()


audio_file = r'C:\Users\saulg\Desktop\alarma.wav'
detect_alarm(audio_file)
