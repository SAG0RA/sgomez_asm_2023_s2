function spectrogram_uno()
    % Definir los parámetros de la señal
    fs = 1000; % Frecuencia de muestreo en Hz
    t = 0:1/fs:1-1/fs; % Vector de tiempo

    % Definir las componentes de la señal
    f1 = 100; % Frecuencia de la primera componente en Hz
    A1 = 0.5; % Amplitud de la primera componente
    phi1 = 0; % Fase de la primera componente en radianes

    f2 = 300; % Frecuencia de la segunda componente en Hz
    A2 = 1.0; % Amplitud de la segunda componente
    phi2 = pi/4; % Fase de la segunda componente en radianes

    % Calcular la señal compleja
    x = A1 * exp(1j * (2*pi*f1*t + phi1)) + A2 * exp(1j * (2*pi*f2*t + phi2));

    % Calcular el espectrograma complejo usando specgram
    specgram(x, 256, fs, 256, 192); % Ventana de 256 puntos, avance de 64 puntos

    title('Espectrograma complejo de una señal compleja');
    xlabel('Tiempo (ms)');
    ylabel('Frecuencia (Hz)');

    % Mostrar el gráfico
    colorbar;
    colormap jet;


end
