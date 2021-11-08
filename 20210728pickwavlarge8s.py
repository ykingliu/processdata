from shutil import move
import os
wavpath = 'F:\\20210701语音识别语料-40h\\end-data\\mono\\'
outpath = 'F:\\20210701语音识别语料-40h\\end-data\\large8s\\'
i = 0
j = 0
sum = 0
textpath = 'F:\\20210701语音识别语料-40h\\end-data\\large8s\\text.txt'
# fh = open(textpath, 'w', encoding='utf-8')
for inde in open('contextlib_duration-40h.txt'):
    info = inde.strip().split(' ')
    name = info[0]
    time = float(info[1])
    path1 = os.path.join(wavpath, name)
    path2 = os.path.join(outpath, name)
    if time >= 8:
        i += 1
        sum += time
        # move(path1, path2)
    else:
        j += 1
print(i)
print(sum/3600)
print(j)
