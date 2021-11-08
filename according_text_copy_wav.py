import pandas as pd
from shutil import copy, move
import os

# =========================根据txt文件复制相应的wav到指定的文件夹===========================
# path = "F:\\数据堂标注10h\\处理后\\"
#
# # fh = open('20210630-10h.txt', 'w', encoding='utf-8')
#
# i=0
# sum=0
# with open("contextlib_duration-0630.txt", "r",encoding='utf-8-sig') as f:
#    for line in f.readlines():
#        line.encode()
#        name = line.strip().split(" ")
#        #path1 = "F:\\20210610语音识别新语料\\end-data\\len-large-3-000-处理结束\\8s以上\\"
#        #path2 = 'F:\\20210610语音识别新语料\\end-data\\len-large-3-000-处理结束\\8s以下\\'
#        path3 = 'F:\\数据堂标注10h\\10h\\'
#        wav_path = os.path.join(path, name[0])
#
#        if sum <= 36000:
#            sum += float(name[1])
#            # move(wav_path, path3)
#            # fh.write(line)
#            i += 1
#        else:
#            print(name[0])
#            break
#            #copy(wav_path, path1)
#            #i += 1
#        #else:
#            #copy(wav_path, path2)
#
#
#
#        # if not os.path.exists(wav_path):
#        #     print(wav_path)
#        #     continue
#        # else:
#        #     #print(wav_path)
#        #     copy(wav_path, path3)
#        #     i+=1
# print(i)
# fh.close()



# 根据csv复制对应的音频到指定文件夹
# path = 'F:\\20210610语音识别新语料\\end-data\\time-large-15s\\processed_audio\\'
# topath = 'F:\\20210610语音识别新语料\\end-data\\time-large-15s\\processed_audio\\2\\'
# reader = pd.read_csv('2-process.csv')
#
# j=0
# for i in reader.index:
#     name = reader['file'].iloc[i]
#     path3 = os.path.join(path, name)
#     copy(path3, topath)
#     j += 1
# print(j)


#根据csv复制相应的wav文件到指定文件夹

# path = "E:\\数据集\\提取数据信息\\accli90cerla30-cer30-40\\2\\"
# path1 = "E:\\数据集\\提取数据信息\\accli90cerla30-cer30-40\\30-40\\"
# i=0
# reader = pd.read_csv("2.csv")
# for inde in reader.index:
#     name = reader["file"].iloc[inde]
#     path3 = os.path.join(path1, name)
#     copy(path3, path)
#     i += 1
# print(i)

# ====================根据文本移动音频到指定文件夹===============================

out = 'F:\\20211026\\mono\\20001-\\'
fh = open('F:\\20211026\\20001-.txt', 'r')
# f = open('F:\\20210823语料\\哈尔滨\\cut_wavs\\large15s\\text-pick.txt', 'w', encoding='utf-8')
j = 0
for i in fh.readlines():
    path = 'F:\\20211026\\\mono\\'
    name = i.strip().split(' ')[0]
    text = i.strip().split(' ')[1]
    print(name)
    path = os.path.join(path, name)
    move(path, out)
    # if len(text) >= 15:
    #     copy(path, out)
    #     f.write(i)
    #     j += 1

#     if text.count('不要挂机')>0 or len(text)<15:
#         move(path, out)
#         j += 1
#     else:
#         f.write(i)
# f.close()
print(j)


