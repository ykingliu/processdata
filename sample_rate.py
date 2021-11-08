import ffmpeg
import soundfile as sf
import numpy as np
import librosa
import os
import pandas as pd
import wave
from shutil import copy
# to install librosa package
# > conda install -c conda-forge librosa

from sklearn.metrics.pairwise import cosine_similarity

'''
filename = 'F:\\新一批数据\\7\\wav - 副本\\7731_1260_1596.wav'
newFilename = 'F:\\新一批数据\\7\\base\\7731_1260_1596.wav'

y, sr = librosa.load(filename, sr=None)
#y,sr = sf.read(filename)
y_8k = librosa.resample(y,sr,8000)
print(sr)
#sf.write(newFilename, y_8k,8000)

ffmpeg.input('F:\\新一批数据\\7\\wav - 副本\\7731_1260_1596.wav').output('F:\\新一批数据\\7\\base\\7731_1260_1596.wav', ar=8000).run()
'''

'''
path = 'F:\\新一批数据\\7\\wav - 副本\\'
newpath = 'F:\\新一批数据\\7\\base\\'
path_list = os.listdir(path)
print(path_list)
for file in path_list:
    path1 = os.path.join(path, file)
    path2 = os.path.join(newpath, file)
    y, sr = librosa.load(path1, sr=None)
    if sr != 8000:
        y_8k = librosa.resample(y, sr, 8000)
        librosa.output.write_wav(path2, y_8k, 8000)
        #sf.write(path2, y_8k, 8000)
        '''


def downsampleWav(src, dst, type,inrate, outrate=8000, inchannels=2, outchannels=1):
    import os, wave, audioop
    if not os.path.exists(src):
        print('Source not found!')
        return False

    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))

    try:
        s_read = wave.open(src, 'r')
        s_write = wave.open(dst, 'w')
    except:
        print('Failed to open files!')
        return False

    n_frames = s_read.getnframes()
    print(n_frames)
    data = s_read.readframes(n_frames)

    try:
        converted = audioop.ratecv(data, 2, inchannels, inrate, outrate, None)
        if outchannels == 1 & type == 2:
            converted = audioop.tomono(converted[0], 2, 1, 0)
        else :
            converted = audioop.tomono(converted[0], 2, 0, 1)
    except:
        print('Failed to downsample wav')
        return False

    try:
        s_write.setparams((outchannels, 2, outrate, 0, 'NONE', 'Uncompressed'))
        s_write.writeframes(converted)
        #s_write.writeframes(n_frames)
    except:
        print('Failed to write wav')
        return False

    try:
        s_read.close()
        s_write.close()
    except:
        print('Failed to close wav files')
        return False

    return True

if __name__ == '__main__':
    path = 'F:\\新一批数据\\9\\5\\khz\\'
    newpath = 'F:\\新一批数据\\9\\5\\khz\\mono\\'

    reader = pd.read_csv('./9-large7s-5.csv')
    files = os.listdir(path)
    for inde in reader.index:
    #for inde in files:
        #print(inde)
        #filename = os.path.join(path, inde)
        #newFilename = os.path.join(newpath, inde)
        #print(filename)
        name = str(int(reader["audio_info_id"].loc[inde])) + "_" + str(int(reader["audio_sequence"].loc[inde])) + "_" + str(inde) + ".wav"
        filename = os.path.join(path, name)
        newFilename = os.path.join(newpath, name)

        if not os.path.exists(filename):
            continue
        else:
            y, sr = librosa.load(filename, sr=None)
            audio_type = reader["audio_type"].loc[inde]
            if sr != 8000:
                downsampleWav(filename, newFilename, audio_type, sr)




'''
#余弦相似度计算

def cos_sim(vector_a, vector_b):
    """
    计算两个向量之间的余弦相似度
    :param vector_a: 向量 a
    :param vector_b: 向量 b
    :return: sim
    """
    vector_a = np.mat(vector_a)
    vector_b = np.mat(vector_b)
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim

wav_path="F:\\data-clean\\new\\00-15\\wav\\s1_862_128.wav"
data, sr = sf.read(wav_path, dtype=np.int16)
data1=data[:,0].reshape(1,-1)
data2=data[:,1].reshape(1,-1)

print(cosine_similarity(data1,data2))

'''
# data1=data[:,0]
# data2=data[:,1]
# print(data1)
# print(data2)
# print(cos_sim(data1, data2))

'''
"""
        左右声道分割
        """
# 读取文本信息
# reader = pd.read_csv('./0-15-0.2-1.csv')
# reader = pd.read_csv('./15-30-0.7-1.csv')
# audioinfo = pd.read_csv('./音频信息.csv')
reader = pd.read_csv('./7-lager4.csv')
for inde in reader.index:
    print(inde)
    # 读取路径
    # wav_path = "F:\\data-clean\\audio\\little15\\wav\\"
    wav_path = "F:\\新一批数据\\7\\wav\\"
    mono_wav = "F:\\新一批数据\\7\\mono-wav\\"
    name = str(reader['audio_info_id'].loc[inde]) + "_" + str(reader['audio_sequence'].loc[inde]) + "_" + str(
        inde) + ".wav"
    wav_path = os.path.join(wav_path, name)
    print(wav_path)
    mono_wav = os.path.join(mono_wav, name)

    # 保存路径
    # 左声道
    # savel_path = "F:\\data-clean\\audio\\little15\\wav1\\"
    # savel_path = "F:\\data-clean\\new\\00-15\\wav1\\"
    # namel = str(reader['audio_info_id'].loc[inde]) + "_" + str(reader['audio_sequence'].loc[inde]) + ".wav"
    # wavl_path = os.path.join(savel_path, namel)
    # print(wavl_path)

    # 右声道
    # saver_path = "F:\\data-clean\\audio\\little15\\wav2"
    # saver_path = "F:\\data-clean\\new\\00-15\\wav2\\"
    # namer = str(reader['audio_info_id'].loc[inde]) + "_" + str(reader['audio_sequence'].loc[inde]) + ".wav"
    # wavr_path = os.path.join(saver_path, namer)
    # print(wavr_path)

    #id = reader["audio_info_id"].loc[inde]
    # ha = audioinfo[audioinfo["audio_info_id"].isin([id])].index.values[0]
    # print(ha)

    # 读取音频
    # data, sr = sf.read(wav_path, dtype=np.int16)

    # 判断声道数
    d = wave.open(wav_path).getnchannels()
    # print(d)

    # 对于原本单声道音频输出路径
    # wav3_path ='F:\\data-clean\\audio\\little15\\wav3\\'
    wav3_path = 'F:\\新一批数据\\7\\base\\'
    # wav3_path = os.path.join()

    if d == 1:
        copy(wav_path, wav3_path)
    else:
        # 读取音频
        data, sr = sf.read(wav_path, dtype=np.int16)
        if reader["audio_type"].loc[inde] == 1:  # 判断是法务
            sf.write(mono_wav, data[:, 1], samplerate=8000)

        else:  # 债务人
            sf.write(mono_wav, data[:, 0], samplerate=8000)
            '''
