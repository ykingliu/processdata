import pandas as pd
from pydub import AudioSegment
import soundfile as sf
import os
import numpy as np


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
        word.set_frame_rate(8000).export(part_wav_path, format="wav")
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
        word.set_frame_rate(8000).export(part_wav_path, format="wav")

def left_right(audio_path, name, role):
    '''
    保留左声道或者右声道 1：法务 右声道 2：债务人 左声道
    :param audio_path:
    :return:
    '''
    # 保存路径
    path = 'F:\\20210610语音识别新语料\\new_audio\\问题音频\\change\\len-lar3\\l-r\\'
    out_path = os.path.join(path, name)
    # 读取音频
    data, sr1 = sf.read(audio_path, dtype=np.int16)
    # 保存音频
    if role == 2:
        sf.write(out_path, data[:, 0], samplerate=8000) # 提取左声道
    else:
        sf.write(out_path, data[:, 1], samplerate=8000) # 提取右声道

if __name__ == '__main__':
    reader = pd.read_csv('adq_audio_text_part_202106101735.csv')
    reader1 = pd.read_csv('adq_audio_info_202106101728.csv')

    for inde in reader1.index:
        audio_name = reader1['audio_name'].loc[inde]
        if audio_name.find('本人')>0 or audio_name.find('联系人')>0:
            id = reader1['audio_info_id'].loc[inde]
            print(audio_name)
            print(id)
            #new_csv = reader[reader['audio_info_id']==id]
            #new_csv.to_csv('./' + str(id) + '.csv')
            reade = pd.read_csv('./' + str(id) + '.csv')
            for i in reade.index:
                path = 'F:\\20210610语音识别新语料\\new_audio\\问题音频\\'
                audio_path = os.path.join(path, audio_name)
                # 判断轨道数
                # 音频路径
                if reader1['case_user_track'].loc[inde] == 0:  # 单声道
                    file_path = "F:\\20210610语音识别新语料\\new_audio\\问题音频\\change\\len-lar3\\mono\\"
                else:  # 双声道
                    file_path = "F:\\20210610语音识别新语料\\new_audio\\问题音频\\change\\len-lar3\\two\\"

                new_name = str(id) + "_" + str(reade['audio_sequence'].loc[i]) + ".wav"

                second_part_wav_path = os.path.join(file_path, new_name)
                # 切割起止时间
                start_time = reade.loc[i]["start_point"]
                end_time = reade.loc[i]["end_point"]

                get_second_pert_wav(audio_path, start_time, end_time, second_part_wav_path)

                if reader1['case_user_track'].loc[inde] == 2:
                    role = reade['audio_type'].loc[i]
                    left_right(second_part_wav_path, new_name, role)





    # for inde in reader.index:
    #     print(inde)
    #     id = reader['audio_info_id'].loc[inde]
    #     # 筛查信息
    #     ha = reader1[reader1["audio_info_id"].isin([id])].index.values[0]
    #
    #     # 判断轨道数
    #     # 音频路径
    #     if reader1['case_user_track'].loc[ha] == 0: # 单声道
    #         path = "F:\\20210610语音识别新语料\\new_audio\\track1\\"
    #         file_path = "F:\\20210610语音识别新语料\\end-data\\orl-mono\\"
    #     else: # 双声道
    #         path = "F:\\20210610语音识别新语料\\new_audio\\track2\\"
    #         file_path = "F:\\20210610语音识别新语料\\end-data\\cut-audio\\"
    #
    #     audio_name = reader1['audio_name'].loc[ha]
    #     wav_path = os.path.join(path, audio_name)
    #
    #     # 剪切音频存储路径
    #     #file_path = "F:\\20210610语音识别新语料\\cut-audio\\"
    #     new_name = str(id) + "_" + str(reader['audio_sequence'].loc[inde]) + ".wav"
    #     # 保存路径
    #     second_part_wav_path = os.path.join(file_path, new_name)
    #     #print(second_part_wav_path)
    #
    #     # 切割起止时间
    #     start_time = reader.loc[inde]["start_point"]
    #     end_time = reader.loc[inde]["end_point"]
    #     # 切割 法务在右声道、债务人在左声道
    #     if not os.path.exists(wav_path):
    #         continue
    #     else:
    #         get_second_pert_wav(wav_path, start_time, end_time, second_part_wav_path)
    #
    #     if reader1['case_user_track'].loc[ha] == 2:
    #         role = reader['audio_type'].loc[inde]
    #         left_right(second_part_wav_path, new_name, role)