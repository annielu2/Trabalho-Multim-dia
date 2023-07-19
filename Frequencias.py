from scipy.io import wavfile
from os import listdir,scandir
from os.path import isfile, join
from scipy.fft import *
import numpy as np

def freq(file, start_time, end_time):
    
    # Open the file and convert to mono
    sr, data = wavfile.read(file)
    if data.ndim > 1:
        data = data[:, 0]
    else:
        pass

    # Return a slice of the data from start_time to end_time
    dataToRead = data[int(start_time * sr / 1000) : int(end_time * sr / 1000) + 1]

    # Fourier Transform
    N = len(dataToRead)
    yf = rfft(dataToRead)
    xf = rfftfreq(N, 1 / sr)

    # Uncomment these to see the frequency spectrum as a plot
    # plt.plot(xf, np.abs(yf))
    # plt.show()

    # Get the most dominant frequency and return it
    idx = np.argmax(np.abs(yf))
    freq = xf[idx]
    return freq   

def get_frequencies():
    waves = []
    frequencies = []

    actors_dir = 'Audio_Song_Actors_01-24'
    for it in scandir(actors_dir):
        if it.is_dir():
            wavefiles = [f for f in listdir(it.path) if isfile(join(it.path, f))]
            for i in range(len(wavefiles)):
                wavefiles[i] = it.path +"/"+ wavefiles[i]
            waves += wavefiles

    for w in waves:
        file = open(w, 'rb')
        frequencies.append(freq(file, 1000, 2100))      
        file.close
    
    return frequencies