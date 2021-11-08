# coding: utf-8
from pydub import AudioSegment
import wave
import pandas as pd
import os
import soundfile as sf
from shutil import copy
import numpy as np
import librosa

def get_second_pert_wav(main_wav_path, start_time, end_time, part_wav_path):
    '''
    音频切分
    :param main_wav_path: 原音频文件路径
    :param start_time: 截取的开始时间
    :param end_time: 截取的结束时间
    :param part_wav_path: 截取后的音频路径
    :return:
    '''
    start_time = int(start_time*1000)
    end_time = int(end_time*1000)


    #音频格式判断
    t = open(main_wav_path, "rb")
    fileStr = t.read()
    t.close()
    head3Str = fileStr[:3]
    #head = head3Str.decode()
    #head = str(head3Str)
    print(head3Str)
    #print(main_wav_path)




    #判断开头是否为ID3
    if main_wav_path.find(".mp3")>0:
        print("*****mp3****")
        print(main_wav_path)
        sound = AudioSegment.from_file(main_wav_path)
        word = sound[start_time:end_time]
        #word = word.set_channels(1)
        word.export(part_wav_path, format="wav")
    else:
        print("####wav-m4q-amr####")
        print(main_wav_path)
        sound = AudioSegment.from_file(main_wav_path)
        word = sound[start_time:end_time]
        word.export(part_wav_path, format="wav")

def downsampleWav(src, dst, type, inrate, outrate=8000, inchannels=2, outchannels=1):
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
    # 读取csv文本
    #reader = pd.read_csv('./15-30-0.7-1.csv')
    reader = pd.read_csv('./9-large7s-5.csv')
    audioinfo = pd.read_csv('./audio_info (1).csv')
    #audioinfo["audio_name"].loc[1] = "api0090001352115898746487795M23H-Q-13006916857-20200519155104-15285075161.mp3"
    print(reader.shape)

    #wav_path = "D:\\软件\\66fcb1e2967811ea8331ac1f6ba547a8.wav"
    #wav_path = "F:\\data-clean\\audio\\118111.wav"

    for inde in reader.index:
        print(inde)
        #音频所在路径
        # 新一批音频
        wav_path = "F:\\新一批数据\\9\\9-0\\9-0\\"
        # 老一批音频
        #wav_path = "F:\\data-clean\\audio-1\\"

        #id = int(reader["audio_info_id"].loc[inde])
        id = reader["audio_info_id"].loc[inde]
        print(id)
        #上述id在audio_info中的哪行
        ha = audioinfo[audioinfo["audio_info_id"].isin([id])].index.values[0]
        #print(ha)
        #print(audioinfo["audio_name"].loc[1])
        if audioinfo["audio_name"].loc[ha].find(".mp3") > 0:
            wav_name = str(id) + ".mp3"
            #wav_name = audioinfo["audio_name"].loc[ha]
            wav_path = os.path.join(wav_path, wav_name)
        #elif audioinfo["audio_name"].loc[ha].find(".m4a") > 0:
        #    wav_name = str(id) + ".m4a"
        #   wav_path = os.path.join(wav_path, wav_name)
        else:
            wav_name = str(id) + ".wav"
            wav_path = os.path.join(wav_path, wav_name)

        print(wav_path)
        #剪切音频存储路径
        file_path = "F:\\新一批数据\\9\\5\\wav\\"
        #file_path = "F:\\data-clean\\new\\00-15\\wav\\"
        #新一批数据命名
        name =  str(int(reader["audio_info_id"].loc[inde])) + "_" + str(int(reader["audio_sequence"].loc[inde]))+ "_" + str(inde) + ".wav"
        #老一批数据命名
        #name = str(reader["audio_info_id"].loc[inde]) + "_" + str(reader["audio_sequence"].loc[inde])+ ".wav"
        second_part_wav_path = os.path.join(file_path, name)

        start_time = reader.loc[inde]["start_point"]
        end_time = reader.loc[inde]["end_point"]
        if not os.path.exists(wav_path):
            continue
        else:
            get_second_pert_wav(wav_path, start_time, end_time, second_part_wav_path)


    """
        左右声道分割
        """
    # 读取文本信息
    # reader = pd.read_csv('./0-15-0.2-1.csv')
    # reader = pd.read_csv('./15-30-0.7-1.csv')
    # audioinfo = pd.read_csv('./音频信息.csv')
    fh = open('9-5.txt', 'w', encoding='utf-8')

    for inde in reader.index:
        print(inde)
        # 读取路径
        # wav_path = "F:\\data-clean\\audio\\little15\\wav\\"
        wav_path = "F:\\新一批数据\\9\\5\\wav\\"
        mono_wav = "F:\\新一批数据\\9\\5\\mono_wav\\"
        name = str(reader['audio_info_id'].loc[inde]) + "_" + str(reader['audio_sequence'].loc[inde]) + "_" +str(inde) + ".wav"
        wav_path = os.path.join(wav_path, name)
        print(wav_path)
        mono_wav = os.path.join(mono_wav, name)
        ppath = "F:\\新一批数据\\9\\5\\khz\\"
        dpath = "F:\\新一批数据\\9\\5\\khz\\mono\\"

        if not os.path.exists(wav_path):
            continue
        else:
            # 提取文本
            hab = str(int(reader["audio_info_id"].loc[inde])) + "_" + str(
                int(reader["audio_sequence"].loc[inde])) + "_" + str(inde) + ".wav"
            # print(hab)
            hb = hab + " " + reader["audio_text"].loc[inde]
            # print(hb)

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
                wav3_path = 'F:\\新一批数据\\9\\base\\'
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

'''
        y, sr = librosa.load(wav_path, sr=None)
        if sr != 8000:
            copy(wav_path, ppath)
            continue
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
                data, sr = sf.read(wav_path, dtype=np.int16)
                if reader["audio_type"].loc[inde] == 1:  # 判断是法务
                    sf.write(mono_wav, data[:, 1], samplerate=8000)

                else:  # 债务人
                    sf.write(mono_wav, data[:, 0], samplerate=8000)
                '''




