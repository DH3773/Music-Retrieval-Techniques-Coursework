
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

def sinusoid(freq=440, nsamples=2048, srate=22050, amp=1.0, phase = 0.0): 
    dur = nsamples/srate
    t = np.linspace(0,dur,int(srate*dur))
    data = amp * np.sin(2*np.pi*freq *t+phase)
    return data

def bin2freq(k,nsamples,srate): 
    return k*srate/nsamples

nsamples = 2048
srate = 22050
bin1 = 30 
bin2 = 30.5 

# caclulate the frequencies and corresponding sinusoids 
f1 = bin2freq(bin1,nsamples,srate)
f2 = bin2freq(bin2,nsamples,srate)
s1 = sinusoid(freq=f1, nsamples = nsamples)
s2 = sinusoid(freq=f2, nsamples = nsamples)

# calculate the magnitude spectra 
mspec1 = 2 * np.abs(np.fft.fft(s1))/nsamples
mspec2 = 2 * np.abs(np.fft.fft(s2))/nsamples

def simple_spec_plot(spectrum, start_bin, end_bin): 
    plt.figure(figsize=(12,4))
    plt.xlabel('Frequency bin')
    plt.ylabel('Amplitude')
    plt.title('Magnitude Spectrum')
    nsamples = spectrum.shape[0]
    faxis = np.arange(0, nsamples)
    
    # add appropriate plt.plot command after this comment 
    plt.plot(faxis[start_bin:end_bin], spectrum[start_bin:end_bin])

    
    return plt

start_bin = 20
end_bin = 40

p1 = simple_spec_plot(mspec1, start_bin, end_bin)
plt1 = p1.gca()
p1.savefig('mspec1.png', format='png')
p1.show()

p2 = simple_spec_plot(mspec2, start_bin, end_bin)
plt2 = p2.gca()
p2.savefig('mspec2.png', format='png')
p2.show()





