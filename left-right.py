import os
import pandas as pd
import librosa
from shutil import copy
import wave
import soundfile as sf
import numpy as np


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
    '''
    path = 'F:\\新一批数据\\7\\wav - 副本\\'
    newpath = 'F:\\新一批数据\\7\\base\\'

    reader = pd.read_csv('./7-lager4.csv')
    for inde in reader.index:
        name = str(int(reader["audio_info_id"].loc[inde])) + "_" + str(int(reader["audio_sequence"].loc[inde])) + "_" + str(inde) + ".wav"
        filename = os.path.join(path, name)
        newFilename = os.path.join(newpath, name)
        y, sr = librosa.load(filename, sr=None)
        audio_type = reader["audio_type"].loc[inde]
        if sr != 8000:
            downsampleWav(filename, newFilename, audio_type, sr)
    '''
    #"""
    #    左右声道分割
    #"""
    # 读取文本信息

    reader = pd.read_csv('./8-lager7s.csv')
    audioinfo = pd.read_csv('./audio_info (1).csv')
    fh = open('8-6050-17500.txt', 'w', encoding='utf-8')
    for inde in range(6051, 17500):
        print(inde)
        # 读取路径
        # wav_path = "F:\\data-clean\\audio\\little15\\wav\\"
        wav_path = "F:\\新一批数据\\8\\wav\\"
        mono_wav = "F:\\新一批数据\\8\\6050-17500\\"
        name = str(reader['audio_info_id'].loc[inde]) + "_" + str(reader['audio_sequence'].loc[inde]) + "_" +str(inde) + ".wav"
        wav_path = os.path.join(wav_path, name)
        print(wav_path)
        mono_wav = os.path.join(mono_wav, name)
        print(mono_wav)
        ppath = "F:\\新一批数据\\8\\khz\\"
        dpath = "F:\\新一批数据\\8\\khz\\mono\\"

        #y, sr = librosa.load(wav_path, sr=None)
        #audio_type = reader["audio_type"].loc[inde]
        if not os.path.exists(wav_path):
            continue
        else:
            #提取文本
            hab = str(int(reader["audio_info_id"].loc[inde])) + "_" + str(
                int(reader["audio_sequence"].loc[inde])) + "_" + str(inde) + ".wav"
            #print(hab)
            hb = hab + " " + reader["audio_text"].loc[inde]
            #print(hb)

            fh.write(hb)
            fh.write('\n')

            y, sr = librosa.load(wav_path, sr=None)
            audio_type = reader["audio_type"].loc[inde]
            if sr != 8000:
                copy(wav_path, ppath)
                downsampleWav(wav_path, dpath, audio_type, sr)

            else:
                id = reader["audio_info_id"].loc[inde]
                ha = audioinfo[audioinfo["audio_info_id"].isin([id])].index.values[0]
            # print(ha)

            # 读取音频
            # data, sr = sf.read(wav_path, dtype=np.int16)

                # 判断声道数
                d = wave.open(wav_path).getnchannels()
            # print(d)

            # 对于原本单声道音频输出路径
            # wav3_path ='F:\\data-clean\\audio\\little15\\wav3\\'
                wav3_path = 'F:\\新一批数据\\8\\base\\'
            # wav3_path = os.path.join()

                if d == 1:
                    copy(wav_path, wav3_path)
                else:
                    # 读取音频
                    data, sr1 = sf.read(wav_path, dtype=np.int16)
                    if reader["audio_type"].loc[inde] == 1:  # 判断是法务
                        sf.write(mono_wav, data[:, 1], samplerate=8000)

                    else:  # 债务人
                        sf.write(mono_wav, data[:, 0], samplerate=8000)

    fh.close()