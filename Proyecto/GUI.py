import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from analisisEspectralGUI import *


# Crear la ventana principal de la GUI
window = tk.Tk()
window.title("Generador de Espectrogramas")

# Botón para cargar un archivo de audio y generar el espectrograma original
generate_button = tk.Button(
    window, text="Cargar Archivo y Generar Espectrograma Original", command=browse_file)
generate_button.pack(pady=20)

# Botón para manipular la fase del espectrograma

manipulate_button1 = tk.Button(
    window, text="Desplazar la Fase", command=manipulate_phase_shift)
manipulate_button1.pack(pady=10)


manipulate_button2 = tk.Button(
    window, text="Fase cuadratica", command=manipulate_phase_cuadratico)
manipulate_button2.pack(pady=10)

manipulate_button3 = tk.Button(
    window, text="Efecto Flange", command=manipulate_phase_flanger)
manipulate_button3.pack(pady=10)

# Botón para cerrar la aplicación
exit_button = tk.Button(window, text="Salir", command=window.quit)
exit_button.pack()

window.mainloop()