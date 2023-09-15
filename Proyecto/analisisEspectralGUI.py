import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Variables globales para almacenar datos del espectrograma original y modificado
original_spec = None
modified_spec = None

def generate_original_spectrogram(file_path):
    global original_spec
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
    _, _, Sxx, _ = plt.specgram(audio_data, NFFT=nfft, Fs=sample_rate, noverlap=overlap, cmap='hot')

    # Configuración de la representación gráfica del espectrograma original
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Frecuencia (Hz)')
    plt.title('Espectrograma de la Señal de Audio Original')
    plt.colorbar(label='Intensidad (dB)')

    # Almacena la matriz del espectrograma original
    original_spec = Sxx

    # Muestra el espectrograma original en una ventana separada
    plt.show()

def manipulate_phase_invert():
    global modified_spec
    if original_spec is not None:
        # Aplicación de manipulación de fase (en este caso, simplemente se invierte la fase)
        phase = np.angle(original_spec)
        modified_phase = -phase  # Invertir la fase
        modified_spec = np.abs(original_spec) * np.exp(1j * modified_phase)

        # Configuración de la representación gráfica del espectrograma modificado
        plt.figure()
        overlap = 512
        nfft = 1024
        plt.specgram(modified_spec, NFFT=nfft, Fs=sample_rate, noverlap=overlap, cmap='hot')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Frecuencia (Hz)')
        plt.title('Espectrograma de la Señal de Audio con Fase Modificada')
        plt.colorbar(label='Intensidad (dB)')

        # Muestra el espectrograma modificado en una ventana separada
        plt.show()
    else:
        print("Primero debes generar el espectrograma original.")

def manipulate_phase_random():
    global modified_spec
    if original_spec is not None:
     # Aplicación de manipulación de fase: aleatorización de fase
        phase = np.angle(original_spec)
        random_phase = 2 * np.pi * np.random.random(phase.shape) - np.pi  # Fase aleatoria en el rango [-pi, pi]
        modified_spec = np.abs(original_spec) * np.exp(1j * random_phase)

        # Configuración de la representación gráfica del espectrograma modificado
        plt.figure()
        overlap = 512
        nfft = 1024
        plt.specgram(modified_spec, NFFT=nfft, Fs=sample_rate, noverlap=overlap, cmap='hot')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Frecuencia (Hz)')
        plt.title('Espectrograma de la Señal de Audio con Fase Modificada')
        plt.colorbar(label='Intensidad (dB)')

        # Muestra el espectrograma modificado en una ventana separada
        plt.show()
    else:
        print("Primero debes generar el espectrograma original.")
        
def manipulate_mag():
    global modified_spec
    if original_spec is not None:
       # Aplicación de manipulación de fase: inversión de componentes de frecuencia
        magnitude = np.abs(original_spec)
        random_magnitude = magnitude * np.random.uniform(0.5, 1.5, magnitude.shape)  # Factor de aleatorización en el rango [0.5, 1.5]
        modified_spec = random_magnitude * np.exp(1j * np.angle(original_spec))

        # Configuración de la representación gráfica del espectrograma modificado
        plt.figure()
        overlap = 512
        nfft = 1024
        plt.specgram(modified_spec, NFFT=nfft, Fs=sample_rate, noverlap=overlap, cmap='hot')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Frecuencia (Hz)')
        plt.title('Espectrograma de la Señal de Audio con Fase Modificada')
        plt.colorbar(label='Intensidad (dB)')

        # Muestra el espectrograma modificado en una ventana separada
        plt.show()
    else:
        print("Primero debes generar el espectrograma original.")

def browse_file():
    global sample_rate, audio_data
    file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
    if file_path:
        sample_rate, audio_data = wavfile.read(file_path)
        generate_original_spectrogram(file_path)

# Crear la ventana principal de la GUI
window = tk.Tk()
window.title("Generador de Espectrogramas")

# Botón para cargar un archivo de audio y generar el espectrograma original
generate_button = tk.Button(window, text="Cargar Archivo y Generar Espectrograma Original", command=browse_file)
generate_button.pack(pady=20)

# Botón para manipular la fase del espectrograma
manipulate_button = tk.Button(window, text="Invertir Fase", command=manipulate_phase_invert)
manipulate_button.pack(pady=10)

manipulate_button2 = tk.Button(window, text="Aleatorizar Fase", command=manipulate_phase_random)
manipulate_button2.pack(pady=10)


# Botón para cerrar la aplicación
exit_button = tk.Button(window, text="Salir", command=window.quit)
exit_button.pack()

window.mainloop()
