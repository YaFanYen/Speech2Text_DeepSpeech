import os 
import wave
import subprocess
import numpy as np
import editdistance
from deepspeech import Model
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

model    = 'models/deepspeech-0.9.3-models.pbmm'
ds = Model(model) 

data_path = '/home/ed716/Documents/NewSSD/Cocktail/audio/speech2text/resources/diff_gender'
gender = os.listdir(data_path)
transcript_path = '/home/ed716/Documents/NewSSD/Cocktail/audio/speech2text/text.txt'
save_path = '/home/ed716/Documents/NewSSD/Cocktail/audio/speech2text'

f = open(transcript_path, 'r')
id = []
transcripts = []
for line in f:
    id.append(line[:29])
    transcripts.append(line[31:])

x = []
y = []
word_error_count = 0
word_count = 0
for j in range(len(gender)):
    data = os.path.join(data_path, gender[j])
    dataset = os.listdir(data)
    for i in range(len(dataset)):
        if gender[j] == 'male':
            x.append(0)
        elif gender[j] =='female':
            x.append(1)

        audio = data + '/' + dataset[i]
        fin = wave.open(audio, 'rb')
        fs = fin.getframerate()
        audio = np.frombuffer(fin.readframes(fin.getnframes()), np.int16)
        fin.close()
        words = ds.stt(audio)

        if dataset[i].endswith('_s1.wav'):
            dataset[i] = dataset[i][4:29] + '.wav'
        elif dataset[i].endswith('_s2.wav'):
            dataset[i] = dataset[i][29:54] + '.wav'
        index = id.index(dataset[i])
        ref_words = transcripts[index]

        word_error_count += editdistance.eval(ref_words, words)
        word_count += len(ref_words)
        wer = 100 * float(word_error_count) / word_count
        y.append(wer)

plt.scatter(x, y)
plt.xlabel('gender')
plt.ylabel('wer')
x_major_locator = MultipleLocator(1)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.xlim(-1, 2)
plt.savefig('plot.png')
