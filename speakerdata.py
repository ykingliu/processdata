import pandas as pd
from shutil import copy
import os

reader = pd.read_csv('./8-lager7s.csv')

#根据csv文件复制相应的wav到指定的文件夹
#path = "F:\\新一批数据\\9\\1\\mono_wav\\5000-11-2-7\\"
wav_path = "F:\\新一批数据\\8\\mono-wav\\"
#file = "F:\\新一批数据\\8\\speaker\\"

def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder...  ---")
        print("---  OK  ---")

    else:
        print("---  There is this folder!  ---")

#for inde in reader.index:
for inde in range(65000):
    print(inde)
    name = str(int(reader["audio_info_id"].loc[inde])) + "_" + str(int(reader["audio_sequence"].loc[inde])) + "_" + str(
        inde) + ".wav"
    wav_path1 = os.path.join(wav_path, name)
    print(wav_path1)
    # 1:表示法务 2：表示债务人
    if reader["audio_type"].loc[inde] == 1:
        #file = "F:\\新一批数据\\8\\speaker\\" + str(reader["audio_info_id"].loc[inde]) + "\\" + "1" + "\\"
        file = "F:\\新一批数据\\8\\speaker\\" + str(reader["audio_info_id"].loc[inde]) + "_1" + "\\"
        #print(file)
        #mkdir(file)
        name1 = str(int(reader["audio_info_id"].loc[inde])) + "_" + str(int(reader["audio_type"].loc[inde])) + "_" + str(
        inde) + ".wav"
        #path = os.path.join(file, name1)
        if not os.path.exists(wav_path1):
            #print(wav_path)
            continue
        else:
            mkdir(file)
            print(wav_path1)
            copy(wav_path1, file + name1)
        #copy(wav_path1, path)

    else:
        #file = "F:\\新一批数据\\8\\speaker\\" + str(reader["audio_info_id"].loc[inde]) + "\\" + "2" + "\\"
        file = "F:\\新一批数据\\8\\speaker\\" + str(reader["audio_info_id"].loc[inde]) + "_2" + "\\"
        #print(file)
        #mkdir(file)
        name1 = str(int(reader["audio_info_id"].loc[inde])) + "_" + str(
            int(reader["audio_type"].loc[inde])) + "_" + str(
            inde) + ".wav"
        #path = os.path.join(file, name)
        if not os.path.exists(wav_path1):
            #print(wav_path)
            continue
        else:
            mkdir(file)
            print(wav_path1)
            copy(wav_path1, file + name1)









#file = "F:\\新一批数据\\8\\speaker\\"
#mkdir(file)



#copy(wav_path, path)

