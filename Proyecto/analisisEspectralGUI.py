import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def generate_spectrogram(file_path):
    # Carga la señal de audio desde el archivo seleccionado
    sample_rate, audio_data = wavfile.read(file_path)

    # Si el audio es estéreo, conviértelo a mono tomando uno de los canales
    if len(audio_data.shape) == 2:
        audio_data = audio_data[:, 0]  # Toma el canal izquierdo (puedes cambiarlo al derecho si lo prefieres)

    # Parámetros del espectrograma
    window_size = 1024
    overlap = 512
    nfft = 1024

    # Calcula el espectrograma utilizando la transformada de Fourier
    Pxx, freqs, bins, im = plt.specgram(audio_data, NFFT=nfft, Fs=sample_rate, noverlap=overlap, cmap='hot')

    # Configuración de la representación gráfica
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Frecuencia (Hz)')
    plt.title('Espectrograma de la Señal de Audio')
    plt.colorbar(label='Intensidad (dB)')

    # Muestra el espectrograma
    plt.show()

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
    if file_path:
        generate_spectrogram(file_path)

# Crear la ventana principal de la GUI
window = tk.Tk()
window.title("Generador de Espectrogramas")

# Botón para cargar un archivo de audio y generar el espectrograma
generate_button = tk.Button(window, text="Cargar Archivo y Generar Espectrograma", command=browse_file)
generate_button.pack(pady=20)

# Botón para cerrar la aplicación
exit_button = tk.Button(window, text="Salir", command=window.quit)
exit_button.pack()

window.mainloop()

