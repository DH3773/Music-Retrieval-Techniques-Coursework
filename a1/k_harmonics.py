import numpy as np 
import IPython.display as ipd
import matplotlib.pyplot as plt


def create_sinusoid(amp, freq, duration, sample_rate):
    t = np.arange(0, duration, 1.0 / sample_rate)
    return amp * np.sin(2 * np.pi * freq * t)
    
# complete the function k_harmonics  
def k_harmonics(k, amp, freq, duration, sample_rate): 
    data = create_sinusoid(amp, freq, duration*k, sample_rate)

    for K in range(1, k):
        harmonic = create_sinusoid(amp/(1+K), freq*(1+K), duration*k, sample_rate)
        harmonic[:K*int(sample_rate*duration)] = 0
        data += harmonic

    return data

# use the code in a notebook cell to plot/listen to the resulting 
# signal of the k_harmonics function 
f0 = 220
sr = 8000
amp = 0.5
duration = 1 
k = 5 

signal = k_harmonics(k, amp, f0, duration, sr)
# plt.plot(np.abs(signal))
# ipd.Audio(signal, rate=sr)