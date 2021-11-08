import pandas as pd
import shutil
import os
import re

# 去除标点符号
punctuation = '!,;:?"\'、，；'
def removePunctuation(text):
    text = re.sub(r'[{}]+'.format(punctuation),' ',text)
    return text.strip()



reader = pd.read_csv('20210701-4-15s-len-lar6-1.csv')
print(reader.shape)
i = 0
j = 0

#=============================================================================




#=============================================================================
# 根据音频时长挑选音频
# new_csv = reader
# new_csv['duration'] = new_csv['end_point']-new_csv['start_point']
# new =new_csv[new_csv['duration']<=15]
# new = new[new['duration']>=4]
# print(new.shape)
# new.to_csv('20210701-4-15s.csv')
#============================================================================

# 将字符长度不达标的设置为零
# for inde in reader.index:
#     text = removePunctuation(reader['audio_text'].loc[inde]).replace(" ", "")
#     if len(text) <= 6:
#         i += 1
#         reader['duration'].loc[inde] = 0
#
# reader.to_csv('20210701-4-15s-len-lar6.csv')

#============================================================================







# 保存文本
# fh = open('label_pick_text-large15s.txt', 'w', encoding='utf-8')
#
# #new.to_csv('label_segment_large15s.csv')
# i = 0
# for inde in reader.index:
#     path = 'F:\\语音识别错误\\end_data\\'
#     new_name = str(reader['label_transcribe_id'].loc[inde]) + "_" + str(reader['id'].loc[inde]) + ".wav"
#     move_path = os.path.join('F:\\语音识别错误\\end_data_litt3-litt1.5s\\', new_name)
#     path1 = os.path.join(path, new_name)
#     #text_len = removePunctuation(reader['text'].loc[inde])
#
#     text_len = new_csv['text'].loc[inde]
#
#     # if len(text_len) <= 3:
#     #     new_csv['duration'].loc[inde] = 0
#     if new_csv['duration'].loc[inde] > 15:
#         new_csv['duration'].loc[inde] = 0
#
#     if new_csv['duration'].loc[inde] == 0:
#         i += 1
#         line = new_name + " " + removePunctuation(new_csv['text'].loc[inde]).replace(" ", "")
#         fh.write(line + '\n')
# print(i)
# fh.close()
    


    # if duration <= 15:
    #     i += 1
    #     #if len(text_len) > 3:
    #     if duration >= 1.5:
    #         j += 1
    #     shutil.move(path1, move_path)
#     if len(text_len) <= 3:
#         duration = reader['end'].loc[inde] - reader['start'].loc[inde]
#         if os.path.exists(path1):
#             shutil.move(path1, move_path)
#         i += 1
# print(i)

