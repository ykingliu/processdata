import pandas as pd
import re
import os
'''
读取表格中的audio_text
'''

# 去除标点符号
punctuation = '!,;:?"\'、，；'
def removePunctuation(text):
    text = re.sub(r'[{}]+'.format(punctuation),' ',text)
    return text.strip()


# reader = pd.read_csv('./pick-test-2.csv')
reader = pd.read_csv('F:\\20211026\\large-15s.csv')

# 计算音频长度
# new_csv = reader
# new_csv['duration'] = new_csv['end_point'] - new_csv['start_point']
# new = new_csv[new_csv['duration']>15]
# print(new.shape)

# >15总共有3890条

#=======================================================================================================================
# 提取文本

fh = open('F:\\20211026\\large-15s.txt', 'w', encoding='utf-8')
print(reader.shape)
# audioinfo = pd.read_csv('./音频信息.csv')
i = 0
for inde in reader.index:
    print(inde)

    root_path = 'F:\\20211026\\large15\\'
    name = str(reader['audio_info_id'].loc[inde]) + "_" + str(reader['audio_sequence'].loc[inde]) + '.wav'
    audio_path = os.path.join(root_path, name)

    # hb = name + " " + removePunctuation(reader["audio_text"].loc[inde]).replace(" ", "")
    # i += 1
    # fh.write(hb)
    # fh.write('\n')


    if os.path.exists(audio_path):
        hb = name + " " + removePunctuation(reader["audio_text"].loc[inde]).replace(" ", "")
        i += 1
        fh.write(hb)
        fh.write('\n')


    # ha = str(int(reader["audio_info_id"].loc[inde])) + "_" + str(int(reader["audio_sequence"].loc[inde])) + "_" + str(
    #     inde) + ".wav"
    # if len(removePunctuation(reader["audio_text"].loc[inde]).replace(" ", "")) > 3:
    #     ha = str(int(reader["audio_info_id"].loc[inde])) + "_" + str(int(reader["audio_sequence"].loc[inde])) + ".wav"
    #     print(ha)
    #     hb = ha + " " + removePunctuation(reader["audio_text"].loc[inde]).replace(" ", "")
    #     print(hb)
    #     i += 1
    #     fh.write(hb)
    #     fh.write('\n')
fh.close()
print(i)
#=======================================================================================================================

# ===============提取法务和债务人的文本==============
# fh = open('F:\\法务与债务人文本分类对应文本\\20210706-法务-3.txt', 'w', encoding='utf-8') # 法务文本
# zh = open('F:\\法务与债务人文本分类对应文本\\20210706-债务-3.txt', 'w', encoding='utf-8') # 债务文本
#
# # all = open('F:\\法务与债务人文本分类对应文本\\0-1.txt', 'w', encoding='utf-8')
#
# i = 0
# j = 0
# for inde in reader.index:
#     name = str(reader['audio_info_id'].loc[inde]) + "_" + str(reader['audio_sequence'].loc[inde]) + '.wav'
#     text = removePunctuation(reader["audio_text"].loc[inde]).replace(" ", "")
#     if reader['audio_type'].loc[inde] == 1: # 法务 0替换1
#         if len(text) > 0:
#             # 加名字
#             # fh.write(name + ' ' + text + '\t' + str(reader['audio_type'].loc[inde]))
#             # 不加名字
#             # fh.write(text + '\t' + str(0))
#             # label \t text
#             fh.write('法务' + '\t' + text)
#             fh.write('\n')
#             # all.write(text + '\t' + str(reader['audio_type'].loc[inde]))
#             # all.write('\n')
#             i += 1
#     else: # 债务 1替换2
#         if len(text) > 0:
#             # 加名字
#             # zh.write(name + ' ' + text + '\t' + str(reader['audio_type'].loc[inde]))
#             # 不加名字(text \t label)
#             # zh.write(text + '\t' + str(1))
#             # label \t text
#             zh.write('债务' + '\t' + text)
#             zh.write('\n')
#             # all.write(text + '\t' + str(reader['audio_type'].loc[inde]))
#             # all.write('\n')
#             j += 1
#
# fh.close()
# zh.close()
# # all.close()
# print(i)
# print(j)




