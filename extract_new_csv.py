import pandas as pd
import re
'''
音频时长大于15s
'''
reader = pd.read_csv('F:\\20211026\\20211022-1000-text.csv')
new_csv = reader
new_csv['duration'] = new_csv['end_point'] - new_csv['start_point']
new = new_csv[new_csv['duration']>15]
print(new.shape)
new.to_csv('F:\\20211026\\large-15s.csv')




'''
音频时长大于8s小于等于15s,且字数大于四个字
'''

# 去除标点符号
# punctuation = '!,;:?"\'、，；'
# def removePunctuation(text):
#     text = re.sub(r'[{}]+'.format(punctuation),' ',text)
#     return text.strip()
#
# reader = pd.read_csv('F:\\20211026\\20211022-1000-text.csv')
# new_csv = reader
# new_csv['duration'] = new_csv['end_point'] - new_csv['start_point']
# new = new_csv[new_csv['duration']<=15]
# new = new[5<=new['duration']]
# print(new.shape)
# new['tlen'] = 0
# for i in new.index:
#     print(i)
#     print(removePunctuation(new['audio_text'].loc[i]).replace(' ', ''))
#     text_len = len(removePunctuation(new['audio_text'].loc[i]).replace(' ', ''))
#     print(text_len)
#     new['tlen'].loc[i] = text_len
#
# new1 = new[new['tlen']>5]
# print(new1.shape)
# new1.to_csv('F:\\20211026\\8-15s-1000.csv')
# # new.to_csv('F:\\数据堂标注10h\\3-15s.csv')