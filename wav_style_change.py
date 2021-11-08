import pandas as pd
from pydub import AudioSegment
import os

# audioinfo = pd.read_csv('./.csv')

path = "F:\\新一批数据\\7\\7\\m4a\\7731.m4a"
pathout = "F:\\新一批数据\\7\\7\\m4a\\7731-1.wav"

sound = AudioSegment.from_file(path)
sound.export(pathout, format="wav")

'''
for inde in audioinfo.index:
    if audioinfo["url"].loc[inde].find(".amr")>=0:
        wav_path = audioinfo["url"].loc[inde]
        wav_name = wav_path.split("/")[-1]
        path1 = os.path.join(path, wav_name)
        name = audioinfo["audio_info_id"].loc[inde] + ".wav"
        part_wav_path = os.path.join(pathout, name)
        print(part_wav_path)
        sound = AudioSegment.from_file(path1)
        sound.export(part_wav_path, format="wav")
'''
