'''
此脚本无法将最后的时间加入到标签文本中，需要后续手动加入
'''
outfile = 'C:\\Users\\liuyuanqing\\Desktop\\各个模型测试\\vad\\cleandata-label\\ground_truth\\20210419101957_Q_128001_1028_13948918681.txt'
fh = open(outfile.replace('.txt', '-utt2spk'), 'w', encoding='utf-8')
fb = open(outfile.replace('.txt', '-label.txt'), 'w', encoding='utf-8')

name = outfile.strip().split('\\')[-1].replace('.txt', '')
# chname = name.split('_')[1]
# name = name.replace(chname, '002')
print(name)
i = 0
stemp = 0
etemp = 0

for inde in open(outfile):
    start = inde.strip().split('\t')[0]
    end = inde.strip().split('\t')[1]
    first = name + '_' + str(i)
    # if i != 0:
    #     fb.write(name + '_' + str(i-1) + ' ' + name + ' ' + str(stemp) + ' ' + str(start) + '\n')
    #     fh.write(name + '_' + str(i-1) + ' ' + 'non_speech' + '\n')

    fh.write(first + ' ' + 'speech' + '\n')
    fb.write(first + ' ' + name + ' ' + str(start) + ' ' + str(end) + '\n')
    # stemp = end
    # i += 2
    i += 1
fh.close()
fb.close()
