import pandas as pd
import os
from shutil import move

path = 'F:\\20210610语音识别新语料\\end-data\\time-large-15s\\'
reader = pd.read_csv('./duration-large-15s.csv')

i = 0
j = 0
for inde in reader.index:
    root_path = 'F:\\20210610语音识别新语料\\end-data\\len-large-3\\'
    name = str(reader['audio_info_id'].loc[inde]) + "_" + str(reader['audio_sequence'].loc[inde]) + '.wav'
    audio_path = os.path.join(root_path, name)
    if os.path.exists(audio_path):
        move(audio_path, path)
        i += 1
    else:
        print(audio_path)
        j += 1
print(i)
print(j)
'''
符合要求：3836
不符合要求：54（识别文字长度小于3个字）
'''
