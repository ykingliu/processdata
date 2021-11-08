from wrvad import chunk_vad
import pandas as pd
import glob
import os
import time
'''
对于语音进行语音端点检测，切分出非静音部分
'''
# reader = pd.read_csv('录音导出-1000.csv')
#
# L = 'F:\\分割聚类\\左声道-债务人\\'
# R = 'F:\\分割聚类\\右声道-法务\\'
#
# # for i in range(2):
# #     main(3, )
# # path = 'F:\\data-clean\\audio\\little15\\wav1\\s1_859_41.wav'
# # chunk_vad(3, path)
#
# dir_root = 'F:\\分割聚类\\vad\\'
# # 以说话人创建文件夹
# def mkdir(path):
#     folder = os.path.exists(path)
#
#     if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
#         os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
#         print("---  new folder...  ---")
#         print("---  OK  ---")
#
#     else:
#         print("---  There is this folder!  ---")



# 获取所有音频路径
#path = glob.glob(R + '*.wav')
# path = 'F:\\分割聚类\\vad测试\\l_zz828_王艳敏_719.wav'
path = 'F:\\20210823语料\\哈尔滨\\r20210821151018_Q_101023_1011_018689767787.wav'
# print(path[0])
# name = path[0].split("\\")[-1]
# print(name.replace('l_','').replace('.wav',''))
# dir_name = name.replace('l_','').replace('.wav','')
# dir_path = os.path.join(dir_root, dir_name)
# mkdir(dir_path)
out_path = 'F:\\20210823语料\\哈尔滨\\cut_wavs\\fight\\'
start = time.time()
chunk_vad(3, path, out_path)
print(time.time()-start)


# j = 0
# for i in range(len(path)):
#     audio_path = path[i]
#     name = audio_path.split("\\")[-1]
#     dir_name = name.replace('r_', '').replace('.wav', '')
#     dir_path = os.path.join(dir_root, dir_name)
#     out_path = dir_path
#     print(dir_path)
#     mkdir(dir_path)
#     # vad
#     chunk_vad(3, audio_path, out_path)
#     j += 1
# print(f'总数, {j}')




