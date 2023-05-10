import matplotlib.pyplot as plt
import numpy as np
def correlador(signal,T):
    t = np.arange(0,2+T,T)
    waveform = np.zeros(len(t))
    print(len(t))
    for i in range(len(t)):
        if t[i] >= 0 and t[i] <= 1:
            waveform[i] = t[i]
        elif t[i] > 1 and t[i] <= 2:
            waveform[i] = 2 - t[i]
        else:
            waveform[i] = 0
    min_len = len(signal) if len(signal)<len(waveform) else len(waveform)
    corr = 0
    for i in range(min_len):
        corr +=  signal[i] * waveform[i]
    
    plt.plot(t, waveform)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Correlation between signal and waveform')
    plt.grid(True)
    plt.show()
    return corr*T

#signal = [0, 0.25, 0.5, 0.75, 1, 0.75, 0.50, 0.25, 0]
signal = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0]

T = 0.1

print(correlador(signal, T))

