import pandas as pd
import re
import os

'''
分别读取表格中的法务和债务文本
'''

# 去除标点符号
punctuation = '!,;:?"\'、，；'
def removePunctuation(text):
    text = re.sub(r'[{}]+'.format(punctuation),' ',text)
    return text.strip()

reader = pd.read_csv('F:\\20210823语料\\天津\\20210817-20天津.csv')

left = []
right = []

for i in reader.index:
    audio_info_id = reader['audio_info_id'].loc[i]
    audio_type = reader['audio_type'].loc[i]
    text = removePunctuation(reader['audio_text'].loc[i]).replace(" ", "")
    if i == 0:
        id = audio_info_id
        if audio_type == 1:
            left.append(text)
        else:
            right.append(text)
    else:
        if audio_info_id == id:
            if audio_type == 1:
                left.append(text)
            else:
                right.append(text)
        else:
            f = open('F:\\20210823语料\\天津\\mono_test-data_text\\' + str(id) + '-fw.txt', 'w', encoding='utf-8')
            z = open('F:\\20210823语料\\天津\\mono_test-data_text\\' + str(id) + '-zw.txt', 'w', encoding='utf-8')
            st = '\n'
            f.write(st.join(left))
            z.write(st.join(right))
            left = []
            right = []
            id = audio_info_id
            if audio_type == 1:
                left.append(text)
            else:
                right.append(text)
f = open('F:\\20210823语料\\天津\\mono_test-data_text\\' + str(id) + '-fw.txt', 'w', encoding='utf-8')
z = open('F:\\20210823语料\\天津\\mono_test-data_text\\' + str(id) + '-zw.txt', 'w', encoding='utf-8')
st = '\n'
f.write(st.join(left))
z.write(st.join(right))
