import glob

# path = 'F:\\数据堂标注10h\\10h\\*.wav'
path = 'F:\\20210701语音识别语料-40h\\end-data\\large8s\\*.wav'
wavs = glob.glob(path)
print(len(wavs))

# fh = open('10h.txt', 'w', encoding='utf-8')

textpath = 'F:\\20210701语音识别语料-40h\\end-data\\text.txt'
fh = open(textpath, 'w', encoding='utf-8')

j=0

for i in wavs:
    with open("20210701-4-15s-lenlar6.txt", "r", encoding='utf-8-sig') as f:
        for line in f.readlines():
            line.encode()
            name = line.strip().split(" ")
            # print(type(name[0]))
            if i.find(name[0])>0:
                j += 1
                fh.write(line)

print(j)
fh.close()



'''
根据时长挑选文本
'''
# file1=open("F:\\20210610语音识别新语料\\end-data\\len-large-3-000-处理结束\\contextlib_duration.txt","r",encoding='utf-8')
# file2=open("F:\\20210610语音识别新语料\\end-data\\len-large-3-000-文本\\20210615-len-large3.txt","r",encoding='utf-8')
# lines1=file1.readlines()
# lines2=file2.readlines()
#
# # 保存文本
# fh = open('F:\\20210610语音识别新语料\\end-data\\len-large-3-000-处理结束\\8s以上.txt', 'w', encoding='utf-8')
# fl = open('F:\\20210610语音识别新语料\\end-data\\len-large-3-000-处理结束\\8s以下.txt', 'w', encoding='utf-8')
#
# for line1 in lines1:
#     name1 = line1.split(' ')[0]
#     time = line1.split(' ')[1]
#     if float(time) > 8:
#         for line2 in lines2:
#             name2 = line2.split(' ')[0]
#             if name1==name2:
#                 fh.write(line2)
#     else:
#         for line2 in lines2:
#             name2 = line2.split(' ')[0]
#             if name1==name2:
#                 fl.write(line2)
