# Speech2Text_DeepSpeech

## speech2text

Use deepspeech to convert speech to text and save it in .txt file.

Download deepspeech-0.9.3-models and place it under `/models` .

Place your dataset under `/resources/data`

Run `python speech2text.py` to get the text file with format `filename, text` .

## convert

Convert the audio files to sampling rate=16000, since deepspeech only convert the speech with sampling rate=16000.

`python convert.py`

## wer

Compare the word error rate (WER) of different gender.

Use the .txt file generated from `speech2text.py` as ground truth.

Plot it with `python wer.py` .


