import os
from pocketsphinx import AudioFile, get_model_path, get_data_path

model_path = get_model_path()
data_path = get_data_path()

config = {
    'verbose': False,
    'audio_file': 'audio_files\\audio_files_harvard.wav',
    'buffer_size': 2048,
    'no_search': False,
    'full_utt': False,
    'hmm': os.path.join(model_path, 'en-us'),
    'lm': os.path.join(model_path, 'en-us.lm.bin'),
    'dict': os.path.join(model_path, 'cmudict-en-us.dict')
}

audio = AudioFile(**config)
# print(AudioFile)
word = ""
last_count = 0
word_count = 0
for phrase in audio:
    word += f" {str(phrase)}"
    if (word):
        word_count += 1
        print("Word count" + str(word_count))
    if (word_count > 1):
        last_count += 1
        print("Last count" + str(last_count))
print(word)
