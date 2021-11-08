# 处理大于15s音频
from pydub import AudioSegment
import pandas as pd
import os
import math

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
        print(sound)

        # 取得音频的声道数
        channel_count = sound.channels
        print(channel_count)
        # 取得音频文件采样频率
        frames_per_second = sound.frame_rate
        print(frames_per_second)

        word = sound[start_time:end_time]
        #word = word.set_channels(1)
        word.export(part_wav_path, format="wav")
    else:
        print("####wav-m4q-amr####")
        print(main_wav_path)
        sound = AudioSegment.from_file(main_wav_path)

        # 取得音频的声道数
        channel_count = sound.channels
        print(channel_count)
        # 取得音频文件采样频率
        frames_per_second = sound.frame_rate
        print(frames_per_second)

        word = sound[start_time:end_time]
        word.export(part_wav_path, format="wav")


reader = pd.read_csv('F:\\20210823语料\\哈尔滨\\20210823-large15s.csv')

for inde in reader.index:
    # 音频路径
    path = "F:\\20210823语料\\哈尔滨\\cut_wavs\\large15s\\mono\\"
    new_name = str(reader['audio_info_id'].loc[inde]) + "_" + str(reader['audio_sequence'].loc[inde]) + ".wav"
    path1 = os.path.join(path, new_name)

    cut_path = 'F:\\20210823语料\\哈尔滨\\cut_wavs\\large15s\\音频切割\\'
    time = reader['duration'].loc[inde]
    if os.path.exists(path1):
        if time <= 30:
            start = 0
            half = math.ceil(time / 2)
            end = time
            print(half)
            cut_name1 = str(reader['audio_info_id'].loc[inde]) + "_" + str(reader['audio_sequence'].loc[inde]) + "_" + str(start) + ".wav"
            cut_name2 = str(reader['audio_info_id'].loc[inde]) + "_" + str(reader['audio_sequence'].loc[inde]) + "_" + str(half) + ".wav"
            cut_path1 = os.path.join(cut_path, cut_name1)
            cut_path2 = os.path.join(cut_path, cut_name2)
            get_second_pert_wav(path1, start, half, cut_path1)
            get_second_pert_wav(path1, half, end, cut_path2)
        else:
            for index, i in enumerate(range(0, math.ceil(time), 15)):
                start = i
                end = i + 15
                cut_name = str(reader['audio_info_id'].loc[inde]) + "_" + str(reader['audio_sequence'].loc[inde]) + "_" + str(i) + ".wav"
                cut_path1 = os.path.join(cut_path, cut_name)
                if index == len(range(0, math.ceil(time), 15)) - 1:
                    end = time
                    get_second_pert_wav(path1, start, end, cut_path1)
                else:
                    get_second_pert_wav(path1, start, end, cut_path1)
