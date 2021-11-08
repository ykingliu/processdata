# coding: utf-8
from pydub import AudioSegment
import wave
import pandas as pd
import os

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

if __name__ == '__main__':
    reader = pd.read_csv("./双轨录音时长大于10分钟-第三版.csv")
    reader1 = pd.read_csv("./双轨录音时长大于10分钟-第三版-端点信息.csv")

    path = "F:\\emotion\\双轨音频\\"

    L = "F:\\emotion\\L-债务\\"
    R = "F:\\emotion\\R-法务\\"

    L_out = "F:\\emotion\\slice\\L债务\\"
    R_out = "F:\\emotion\\slice\\R法务\\"


    for inde in reader1.index:

        id = reader1["audio_info_id"].loc[inde]

        print(id)
        # 上述id在audio_info中的哪行
        ha = reader[reader["audio_info_id"].isin([id])].index.values[0]
        print(ha)

        # wav_name = reader['audio_url'].iloc[ha].strip().split('/')[-1]
        # wav_path = os.path.join(path, wav_name)

        start_time = reader1.loc[inde]["start_point"]
        end_time = reader1.loc[inde]["end_point"]
        name_id = str(int(reader1.loc[inde]['audio_info_id'])) + "_" + str(int(reader1.loc[inde]['audio_sequence'])) + "_" + str(int(reader1.loc[inde]['audio_type'])) + ".wav"

        if reader1['audio_type'].iloc[inde] == 1: #法务
            name = reader['audio_url'].iloc[ha].strip().split('/')[-1]
            if name.find(".mp3")>0:
                right = "r" + name.replace('.mp3', '.wav')
                r_file = os.path.join(R, right)

            else:
                right = "r" + name
                r_file = os.path.join(R, right)
            second_part_wav_path = os.path.join(R_out, name_id)

            get_second_pert_wav(r_file, start_time, end_time, second_part_wav_path)
        else:
            name = reader['audio_url'].iloc[ha].strip().split('/')[-1]
            if name.find(".mp3") > 0:
                left = "l" + name.replace('.mp3', '.wav')
                l_file = os.path.join(L, left)

            else:
                left = "l" + name
                l_file = os.path.join(L, left)
            second_part_wav_path = os.path.join(L_out, name_id)

            get_second_pert_wav(l_file, start_time, end_time, second_part_wav_path)












        # name = reader['audio_url'].iloc[inde].strip().split('/')[-1]
        # audio_id = reader['audio_info_id'].iloc[inde]
        # new_csv = reader1[reader1['audio_info_id']==audio_id]
        #
        # for i in new_csv.index:
        #     start_time = new_csv['start_point']
        #     end_time = new_csv['end_point']
        #     if new_csv['audio_type'] == 2:
        #     second_path = os.path.join()


