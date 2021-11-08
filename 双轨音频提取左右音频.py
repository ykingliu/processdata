import os
import pandas as pd
import librosa
from shutil import copy
import wave
import soundfile as sf
import numpy as np
from pydub import AudioSegment

reader = pd.read_csv('./录音导出-1000.csv')

path = "F:\\分割聚类\\双轨音频\\"
L = "F:\\分割聚类\\左声道-债务人\\"
R = "F:\\分割聚类\\右声道-法务\\"
mp3 = "F:\\分割聚类\\MP3\\"

i = 0

for inde in reader.index:
    name = reader['audio_url'].iloc[inde].strip().split('/')[-1]
    name1 = reader['case_user_name'].iloc[inde] + '_' + reader['contact_name'].iloc[inde] + '_' + str(inde) + name[-4:]
    name2 = name1.replace('*', '')
    audio_path = os.path.join(path, name2)

    #left = "l" + name
    #right = "r" + name
    if os.path.exists(audio_path):
        if reader['audio_url'].iloc[inde].strip().split('/')[-1].find(".mp3")>0:
            # 将MP3格式音频转为wav格式
            # print(audio_path)
            sound = AudioSegment.from_file(audio_path)
            # audio_path = os.path.join(mp3, reader['audio_url'].iloc[inde].strip().split('/')[-1].replace('.mp3','.wav'))
            audio_path = os.path.join(mp3, name2.replace('.mp3', '.wav'))
            # print(audio_path)
            sound.export(audio_path, format="wav")

            left = "l" + '_' + name2.replace('.mp3','.wav')
            right = "r" + '_' + name2.replace('.mp3','.wav')
            l_file = os.path.join(L, left)
            r_file = os.path.join(R, right)
        else:
            left = "l" + '_' + name2
            right = "r" + '_' + name2
            l_file = os.path.join(L, left)
            r_file = os.path.join(R, right)
        # print(audio_path)
        # print(l_file)
        # print(r_file)
        d = wave.open(audio_path).getnchannels()
        if d == 2:
            i += 1
            data, sr1 = sf.read(audio_path, dtype=np.int16)
            sf.write(l_file, data[:, 0], samplerate=8000)
            sf.write(r_file, data[:, 1], samplerate=8000)
            print(inde)
        else:
            print(audio_path)

print(f'通道数为2， {i}')

# 最终通道数为2:983  最终通道数为1:16





