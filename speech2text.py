from __future__ import absolute_import, division, print_function
import os
import numpy as np
import wave

from deepspeech import Model

model = 'models/deepspeech-0.9.3-models.pbmm'
ds = Model(model) 

data_path = '/home/ed716/Documents/NewSSD/Cocktail/audio/speech2text/resources/data'
dataset = os.listdir(data_path)
save_path = '/home/ed716/Documents/NewSSD/Cocktail/audio/speech2text'

for i in range(len(dataset)):
    audio = data_path + '/' + dataset[i]
    fin = wave.open(audio, 'rb')
    fs = fin.getframerate()
    audio = np.frombuffer(fin.readframes(fin.getnframes()), np.int16)
    fin.close()
    words = ds.stt(audio)

    with open('%s/text.txt'%save_path, 'a') as f:
        f.write('%s, %s'%(dataset[i],words))
        f.write('\n')
