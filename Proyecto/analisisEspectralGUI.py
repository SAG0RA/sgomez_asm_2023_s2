import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from GUI import *

# Variables globales para almacenar datos del espectrograma original y modificado
original_spec = None
modified_spec = None


def generate_original_spectrogram(file_path):
    global original_spec, sample_rate, audio_data
    # Carga la señal de audio desde el archivo seleccionado
    sample_rate, audio_data = wavfile.read(file_path)

    if len(audio_data.shape) == 2:
        audio_data = audio_data[:, 0]

    # Parámetros del espectrograma
    overlap = 512
    nfft = 1024

    # Calcula el espectrograma utilizando la transformada de Fourier
    _, _, Sxx, _ = plt.specgram(
        audio_data, NFFT=nfft, Fs=sample_rate, noverlap=overlap, cmap='hot')

    # Configuración de la representación gráfica del espectrograma original
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Frecuencia (Hz)')
    plt.title('Espectrograma de la Señal de Audio Original')
    plt.colorbar(label='Intensidad (dB)')

    # Almacena la matriz del espectrograma original
    original_spec = Sxx

    # Muestra el espectrograma original en una ventana separada
    plt.show()


def manipulate_phase_shift():
    if original_spec is not None:
        # Calcular el número de muestras a desfasar
        num_muestras_a_desfasar = int(700 * sample_rate)

    # Crear un nuevo arreglo de audio con el desfase
        audio_data_desfasado = np.roll(audio_data, num_muestras_a_desfasar)

        # Configuración de la representación gráfica del espectrograma modificado
        plt.figure()
        duration = len(audio_data_desfasado) / num_muestras_a_desfasar
        # Tamaño de ventana igual a la duración total en muestras
        nfft = int(duration * sample_rate)
        overlap = 512  # No hay superposición para que cada ventana cubra toda la señal
        plt.specgram(audio_data_desfasado, NFFT=nfft, Fs=sample_rate,
                     noverlap=overlap, cmap='hot')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Frecuencia (Hz)')
        plt.title('Espectrograma de la Señal de Audio con Fase Modificada')
        plt.colorbar(label='Intensidad (dB)')

        # Muestra el espectrograma modificado en una ventana separada
        plt.show()

    
    else:
        print("Primero debes generar el espectrograma original.")


def manipulate_phase_cuadratico():
    # Crear un vector de desfase cuadrático
    t = np.arange(len(audio_data)) / sample_rate
    cuadratic_phase = 2 * t**2

    # Aplicar el desfase cuadrático a la fase de la señal
    fase_audio = np.angle(np.fft.fft(audio_data))
    fase_audio_modificada = fase_audio + cuadratic_phase

    # Reconstruir la señal en el dominio del tiempo
    audio_data_modificado = np.fft.ifft(
        np.abs(np.fft.fft(audio_data)) * np.exp(1j * fase_audio_modificada))

    # Configuración de la representación gráfica del espectrograma modificado
    plt.figure()
    duration = len(audio_data_modificado) / int(2000 * sample_rate)

    # Tamaño de ventana igual a la duración total en muestras
    nfft = int(duration * sample_rate)
    overlap = 512

    plt.specgram(audio_data_modificado, NFFT=nfft, Fs=sample_rate,
                 noverlap=overlap, cmap='hot')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Frecuencia (Hz)')
    plt.title('Espectrograma de la Señal de Audio con Fase Modificada')
    plt.colorbar(label='Intensidad (dB)')

    # Muestra el espectrograma modificado en una ventana separada
    plt.show()

def manipulate_phase_flanger():
    depth = 0.4
    rate = 1
     # Crear un vector de tiempo
    tiempo = np.arange(len(audio_data)) / sample_rate

    # Crear la señal moduladora sinusoidal
    moduladora = 1 + depth * np.sin(2 * np.pi * rate * tiempo)

    # Aplicar el efecto flanger multiplicando la señal por la señal moduladora
    audio_data_modificado = audio_data * moduladora

    # Configuración de la representación gráfica del espectrograma modificado
    plt.figure()
    duration = len(audio_data_modificado) / int(2000 * sample_rate)

    # Tamaño de ventana igual a la duración total en muestras
    nfft = int(duration * sample_rate)
    overlap = 512

    plt.specgram(audio_data_modificado, NFFT=nfft, Fs=sample_rate,
                 noverlap=overlap, cmap='hot')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Frecuencia (Hz)')
    plt.title('Espectrograma de la Señal de Audio con Fase Modificada')
    plt.colorbar(label='Intensidad (dB)')

    # Muestra el espectrograma modificado en una ventana separada
    plt.show()

    save_audio(audio_data_modificado)



def browse_file():
    global sample_rate, audio_data
    file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
    if file_path:
        sample_rate, audio_data = wavfile.read(file_path)
        generate_original_spectrogram(file_path)

        
def save_audio(audio_data_modificado):
    # Asegurarse de que los valores estén en el rango adecuado
    audio_data_modificado = np.clip(audio_data_modificado.real, -32768, 32767).astype(np.int16)

    # Guardar el audio modificado en un nuevo archivo WAV
    wavfile.write(r'C:\Users\saulg\Desktop\audio_modificado.wav', sample_rate, audio_data_modificado)

