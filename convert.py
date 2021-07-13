import os

data_path = '/home/ed716/Documents/NewSSD/Cocktail/audio/speech2text/resources/diff_gender/female'
data = os.listdir(data_path)

command = 'cd speech2text/resources/diff_gender/female;'
for i in range(0, len(data)):
    name = data[i]
    f_name = str(name[0:-4])
    command += 'ffmpeg -y -i %s.wav -ar 16000 %s.wav;' % (f_name, f_name)
    #command += 'ffmpeg -y -i %s.m4a ../norm_audio_train_wav/%s.wav;' % (f_name, f_name)
    os.system(command)
