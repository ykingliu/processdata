import wave
import os
import soundfile as sf
import numpy as np
import pandas as pd
from pydub import AudioSegment
import glob
import librosa
from shutil import move, copy

#wav_path = "C:\\Users\\liuyuanqing\\Downloads\\audio\\118111.wav"
#wav_path = "http://192.168.1.178:8099/file/1589954887508/118111.wav"
#wav_path = "F:\\data-clean\\audio\\large15-0.7-1\\wav\\s1_1355_80.wav"
#wav_path = "F:\\data-clean\\audio\\1234.amr"
#2627436_14_0
wav_path1 = "F:\\20210610语音识别新语料\\end-data\\time-large-15s\\切割音频\\2627436_14_0.wav"
#wav_path2 = "F:\\新一批数据\\8\\khz-mono\\8546_78_18454.wav"
#reader = pd.read_csv('./0-15-0.2-1.csv')
#print(reader.shape)
#print(wav_path2)
#with wave.open(wav_path1, "rb") as f:

#path = 'F:\\20210610语音识别新语料\\end-data\\len-large-3-000\\'
path = 'F:\\20210610语音识别新语料\\new_audio\\问题音频\\change\\len-lar3\\l-r\\'
path2 = 'F:\\20210701语音识别语料\\new_audio\\track2\\'
path3 = 'F:\\20210610语音识别新语料\\end-data\\time-large-15s\\切割音频\\'

out = 'F:\\20210610语音识别新语料\\new_audio\问题音频\\change\\len-lar3\\==len-large-3-000\\'
out2 = 'F:\\20210610语音识别新语料\\end-data\\len-large-3-problem\\'
# 对比两个文件夹下的音频数
# for i in glob.glob(path + '/*'):
#     name = i.split('\\')[-1]
#     for j in glob.glob(path2 + '/*'):
#         name2 = j.split('\\')[-1]
#         if name2 == name:
#             move(i, out)



j = 0
for i in glob.glob(path2 + '/*.wav'):
    #print(i)
    f = wave.open((i))
    signal, sr = librosa.load(i, sr=None)
    #print(sr)
            #获取音频信息
    #print(f.getparams())
    samp_width = f.getsampwidth()
    channel = f.getnchannels()
    #print(samp_width)
    #if samp_width != 2:
    if sr != 8000 or samp_width != 2 or channel != 2:
        print(sr)
        j += 1
        print(i)
        #copy(i, out2)
print(j)















#f = wave.open((wav_path2))
        #获取音频信息
#print(f.getparams())
#data, sr = sf.read(wav_path1, dtype=np.int16)
#print(data[:,0].shape)
#print(data[:,1].shape)
#sf.write("F:\\data-clean\\audio\\large15\\s2_6553_235.wav", data[:,0], samplerate=8000)
#sf.write("F:\\data-clean\\audio\\large15\\s2_6553_235-1.wav", data[:,1], samplerate=8000)
#sound = AudioSegment.from_file(wav_path)
#sound = sound.set_channels(1)
#word = sound[start_time:end_time]
#sound.export("F:\\data-clean\\audio\\s1_5120.wav", format="wav")

'''
path = 'F:\\新一批数据\\7\\wav - 副本\\'
newpath = 'F:\\新一批数据\\7\\base\\'
path_list = os.listdir(newpath)
print(path_list)
i=0
for file in path_list:
    path1 = os.path.join(path, file)
    path2 = os.path.join(newpath, file)
    d = wave.open(path1).getnchannels()
    if d ==1:
        print(file)
        i+=1
print(i)
'''