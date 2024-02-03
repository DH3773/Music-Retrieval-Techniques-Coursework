import numpy as np 
import IPython.display as ipd
import matplotlib.pyplot as plt

def create_sinusoid(amp, freq, duration, sample_rate):
    t = np.arange(0, duration, 1.0 / sample_rate)
    return amp * np.sin(2 * np.pi * freq * t)
    
# complete the function k_harmonics  
def harmonics_arpeggiator(r, k, freq, dur, sample_rate):
    data = []
    for R in range (0, r):
        for K in range(1, k+1):
            data = np.concatenate((data, create_sinusoid(1, freq*(K), dur, sample_rate)))
    
    return data



# use the code in a notebook cell to plot/listen to the resulting 
# signal of the k_harmonics function 
f0 = 220
sr = 44100 
duration = 0.125
r = 4 
k = 12 

signal = harmonics_arpeggiator(r, k, f0, duration, sr)

# use in notebook for listening to audio 
ipd.Audio(signal, rate=sr)