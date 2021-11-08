import numpy as np

'''
带有标点的文本语料处理成标点预测的训练语料，标点符号{，|。|？}，其他用O表示
notice: 也可以用于文本分割的处理 标签{b,m,e,s}
'''

# text_path = 'F:\\标点预测\\dt\\train'
text_path = 'F:\\标点预测\\dt2\\valid'
data_path = 'F:\\标点预测\\dt2\\data\\valid'

f = open(text_path, 'r', encoding='UTF-8')
fh = open(data_path, 'w', encoding='UTF-8')

for txt in f.readlines():
    text = txt.strip().split(' ')[1]
    print(text)
    toFind0 = '，'
    comma = list(filter(lambda x: text[x] == toFind0, list(range(len(text)))))  # 将文本中包含逗号的位置定位出来
    toFind1 = '。'
    period = list(filter(lambda x: text[x] == toFind1, list(range(len(text)))))
    toFind2 = '？'
    question = list(filter(lambda x: text[x] == toFind2, list(range(len(text)))))
    comma = np.array(comma) - 1
    period = np.array(period) - 1
    question = np.array(question) - 1
    print(comma)
    print(period)
    print(question)
    i = 0
    for word in text:
        print(word)
        if '，' in word or '。' in word or '？' in word:
            i += 1
            continue
        elif i in comma:
            line = word + '\t' + '，' + '\n'
        elif i in period:
            line = word + '\t' + '。' + '\n'
        elif i in question:
            line = word + '\t' + '？' + '\n'
        else:
            line = word + '\t' + 'O' + '\n'
        fh.write(line)
        i += 1
        print(line)
fh.close()
