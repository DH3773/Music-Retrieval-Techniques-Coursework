import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy import signal



def sinusoid(freq=440, nsamples=2048, srate=22050, amp=1.0, phase = 0.0): 
    dur = nsamples/srate
    t = np.linspace(0,dur,int(srate*dur))
    data = amp * np.sin(2*np.pi*freq *t+phase)
    return data


def generate_tone(freqs, dur=1.0, srate=44100.0):
    data = np.zeros(int(dur*srate))
    for freq in freqs:
        data += sinusoid(freq, dur, srate, np.random.rand(), np.random.rand()*2*np.pi)
    return data


def analyze_tone_dft(freqs, data, srate=44100.0):
    N = len(data)

    #predetermine the linearly spaced frequencies (bins)
    #that will be used in the FFT
    freqs_dft = np.linspace(0, srate, N)
    #compute the DFT of the signal
    dft = np.fft.fft(data)

    #extract the amplitudes and phases of the 3 frequencies
    amplitudes = np.zeros(3)
    phases = np.zeros(3)
    for i, freq in enumerate(freqs):
        #finds closest DFT bin to selected frequency using above predetermined bins
        idx = np.argmin(np.abs(freqs_dft-freq))
        #extract amplitude and phase of the DFT at that bin
        amplitudes[i] = np.abs(dft[idx])/N
        phases[i] = np.angle(dft[idx])
    return amplitudes, phases


def evaluate_analysis(amp_orig, amp_est):
    return np.mean((np.array(amp_orig) - np.array(amp_est))**2)



def analyze_tone_fixed_frequencies(freqs, data, srate=44100.0):
    N = len(data)
    T = 1.0/srate
    #create time vector
    t = np.linspace(0.0, N*T, N, endpoint=False)
    amplitudes = []
    phases = []
    for freq in freqs:
        #compute the DFT of the signal using specified frequencies as basis vectors
        y = np.sum(data * np.exp(-2j * np.pi * freq * t)) / N
        amplitudes.append(np.abs(y))
        phases.append(np.angle(y))
    return amplitudes, phases


