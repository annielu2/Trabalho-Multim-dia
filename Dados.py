import librosa
from os import listdir,scandir
from os.path import isfile, join
from scipy.fft import *
import numpy as np

audios_list = []

def get_audios():
    waves = []
    target = []
    actors_dir = 'speech_data'
    for it in scandir(actors_dir):
        if it.is_dir():
            wavefiles = [f for f in listdir(it.path) if isfile(join(it.path, f))]
            for i in range(len(wavefiles)):
                wavefiles[i] = it.path +"/"+ wavefiles[i]
                emotion = it.path[16:]
                target.append(emotion)
            waves += wavefiles

    for w in waves: 
        #https://s3.ca-central-1.amazonaws.com/assets.jmir.org/assets/preprints/preprint-46970-accepted.pdf
        y, sr = librosa.load(w)
        #calculating zero crossing rate
        zero_crossing_rate = librosa.feature.zero_crossing_rate(y, frame_length=256, hop_length=512, center=True)
        zero_crossing_rate = np.ndarray.tolist(np.ndarray.flatten(zero_crossing_rate))
        #calculating energy
        energy = np.array([
            sum(abs(y[i:i+256]**2))
            for i in range(0, len(y), 512)
        ])
        energy = np.ndarray.tolist(np.ndarray.flatten(energy))
        #calculating mfcc
        mfcc = librosa.feature.mfcc(y=y, sr=sr, S=None, n_mfcc=20, dct_type=2, norm='ortho', lifter=0)
        mfcc = np.ndarray.tolist(np.ndarray.flatten(mfcc))
        features = zero_crossing_rate + energy + mfcc
        audios_list.append(features)

    
    return audios_list, target