import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
frecuencia = 1000  # Frecuencia de la señal en Hz
duracion = 10.0    # Duración de la señal en segundos
amplitud = 1.0    # Amplitud de la señal

# Tasa de muestreo según el teorema de Nyquist-Shannon
tasa_muestreo = 2 * frecuencia

# Tiempo de muestreo
t = np.linspace(0, duracion, int(tasa_muestreo * duracion), endpoint=False)

# Generar una señal senoidal
senal = amplitud * np.sin(2 * np.pi * frecuencia * t)

# Agregar ruido gaussiano a la señal
ruido = np.random.normal(0, 0.5, len(senal))
senal_con_ruido = senal + ruido

# Mostrar la señal original en el dominio del tiempo
plt.figure(figsize=(10, 4))
plt.subplot(2, 1, 1)
plt.plot(t, senal)
plt.title('Señal Original')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

# Mostrar el espectrograma de la señal con ruido
plt.subplot(2, 1, 2)
plt.specgram(senal_con_ruido, Fs=tasa_muestreo, cmap='viridis')
plt.title('Espectrograma de la Señal con Ruido')
plt.xlabel('Tiempo (s)')
plt.ylabel('Frecuencia (Hz)')
plt.colorbar(label='Intensidad (dB)')

plt.tight_layout()
plt.show()