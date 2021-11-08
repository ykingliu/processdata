import librosa
import wave
from scipy.io import wavfile
import numpy as np
change_path = 'C:\\Users\\liuyuanqing\\Downloads\\16k-l_chunk-09.wav'
path = 'F:\\分割聚类\\vad\\bj167_胡敏_146\\l_chunk-09.wav'
audio, sr = librosa.load(path, sr=None)
print(sr)
print(len(audio))
# librosa load音频时 会自动进行32767归一化操作
# 此处和scipy中的wavfile有些区别
print((audio*32767))
y_16k = librosa.resample(audio, sr, 16000)
print(len(y_16k))
data = y_16k*32767
print((data.astype(np.int16)))
out_path = 'F:\\分割聚类\\output.wav'

wavfile.write(out_path, 16000, data.astype(np.int16))

# 其他修改采样率后的音频
print('******工具修改******')
audio1, sr1 = librosa.load(change_path, sr=None)
print(sr1)
print(audio1*32767)
print(len(audio1))

rate1, wav1 = wavfile.read(change_path)
print(rate1)
print(wav1)


# def convert8k_16k():

f = wave.open((path))
        #获取音频信息
print(f.getparams())

rate, wav = wavfile.read(path)
print(rate)
print(wav)
print(len(wav))

#def convert8k_16k():
