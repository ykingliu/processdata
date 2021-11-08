import wave
import glob
from itertools import zip_longest
from pydub import AudioSegment
import random

'''
合成说话人分割聚类数据集
融合两个音频片段为一条音频
'''

# 路径修改
#infiles = ["F:\\分割聚类\\vad\\bj13_刁亚楠_392\\l_chunk-00.wav", "F:\\分割聚类\\vad\\bj13_刁亚楠_392\\r_chunk-00.wav", "F:\\分割聚类\\vad\\bj13_刁亚楠_392\\l_chunk-01.wav"]
outfile = "F:\\分割聚类\\合并测试\\vad-dataset\\data\\演示数据\\hf390_韩媛_460.wav"

audio_seg_1 = glob.glob('F:\\分割聚类\\vad\\筛选完1\\hf390_韩媛_460-筛选完\\l_*.wav')
audio_seg_2 = glob.glob('F:\\分割聚类\\vad\\筛选完1\\hf390_韩媛_460-筛选完\\r_*.wav')

# 噪声片段 198段
noise_seg = glob.glob('F:\\分割聚类\\收集噪声\\*.wav')
print(noise_seg)

# 音乐片段 48段
#noise_seg = glob.glob('F:\\分割聚类\\收集噪声\\音乐\\*.wav')


# print(list(zip(audio_seg_1, audio_seg_2)))
# print(list(zip_longest(audio_seg_1, audio_seg_2)))
# print(len(audio_seg_1))
# print(len(audio_seg_2))

# 通过读入音频的参数计算音频的时长
# h = wave.open('F:\\分割聚类\\vad\\筛选完\\bj13_刁亚楠_392\\l_chunk-02.wav', 'rb')
# print(h.getparams())
# print(h.getnframes())
# print(h.readframes(h.getnframes()))
# print(h.getframerate())
# print(h.getnframes()/float(h.getframerate()))


# 将右声道的法务和左声道的债务人交替放入列表中
info = zip_longest(audio_seg_1, audio_seg_2)
print(list(info))
all = []
for seg1, seg2 in zip_longest(audio_seg_1, audio_seg_2):
    print(seg1)
    print(seg2)
    if seg1 is not None:
        all.append(seg1)
    if seg2 is not None:
        all.append(seg2)

print(all)
print(len(all))

# 创建1s的静音
#one_sec_segment = AudioSegment.silent(duration=1000).set_frame_rate(8000)
#one_sec_segment = one_sec_segment.raw_data
# one_sec_segment.set_frame_rate(8000).export("F:\\分割聚类\\合并测试\\sli.wav", format='wav')
# sli = wave.open("F:\\分割聚类\\合并测试\\sli.wav", 'rb')
# print(f'sli, {sli.getparams()}')


# 一个文件夹下多个音频合并
data = []
time = []
for li in all:
    w = wave.open(li, 'rb')
    fr = w.getframerate()
    nf = w.getnframes()
    length = round((float(nf) / float(fr)), 5)
    print(length)

    # r 法务 l 债务人
    # r_name:r_法务id  l_name:l_法务id
    r_name = li.strip().split('\\')[-2].split('_')[0]
    if li.strip().split('\\')[-1].find('l')>=0:
        name = 'l' + '_' + r_name
        #print(l_name)
    else:
        name = 'r' + '_' + r_name
        #print(r_name)
    # 各个音频片段的间隔
    time.append([name, length])
    data.append([w.getparams(), w.readframes(w.getnframes())])
    i = random.randint(0,1) # 插入音频类型 0：插入静音 1：随机插入噪声
    if i == 0:
        a = random.randint(0, 3) # 随机生成静音参数
        # 产生对应的静音bytes
        one_sec_segment = AudioSegment.silent(duration=(a * 1000)).set_frame_rate(8000)
        one_sec_segment = one_sec_segment.raw_data
        data.append([w.getparams(), one_sec_segment])
        time.append(['sil', a])
    else:
        b = random.randint(0, 197)  # 随机噪声参数
        noise = wave.open(noise_seg[b], 'rb')
        n_fr = noise.getframerate()
        n_nf = noise.getnframes()
        n_length = round((float(n_nf) / float(n_fr)), 5)
        # n_name = noise_seg[b].split("\\")[-1].replace('.wav', '')
        time.append(['noise', n_length])
        data.append([w.getparams(), noise.readframes(noise.getnframes())])
    w.close()
print(len(data))
print(len(time))
print(time)

# 保存对应的转录文件
# 格式：speaker uri 1 start duration <NA> <NA> speaker-id <NA> <NA>
# 随机过程：|---sp---|---n---|---sp---|---sil---|---sp---| ...
#             t1       t2      t3       t4        t5 ...
#         s:0  e:t1      s:t1+t2 e:t1+t2+t3  s:t1+t2+t3+t4  e:t1+t2+t3+t4+t5  ...

k = 0
start = 0.0
uri = outfile.strip().split('\\')[-1].replace('.wav', '')
spk_name = uri.split('_')[1]
# _001_: 001表示加入噪声 _002_: 002表示加入音乐
uri = uri.replace(spk_name, '001')
print(uri)


fh = open(outfile.replace('.wav', '-utt2spk'), 'w', encoding='utf-8')
fb = open(outfile.replace('.wav', '-label.txt'), 'w', encoding='utf-8')
with open(outfile.replace('.wav', '.txt'), 'w', encoding='utf-8') as f:
    i = 0
    for ti in time:
        end = start + ti[1]
        if ti[1] != 0:
            f.write(uri+ '_' + str(i) + ' ' + uri + ' ' + str(round(start, 3)) + ' ' + str(round(end, 3)) + '\n')
            s = str(round(start, 3))
            e = str(round(end, 3))
        start = start + ti[1]
        if ti[0] != 'sil' and ti[0] != 'noise':
            fh.write(uri + '_' + str(i) + ' ' + 'speech' + '\n')
            fb.write(s + '\t' + e + '\t' + 's' + '\n')
            i += 1
        else:
            if ti[1] != 0:
                fh.write(uri+ '_' + str(i) + ' ' + 'non_speech' + '\n')
                fb.write(s + '\t' + e + '\t' + 'n' + '\n')
                i += 1
        # if ti[0] != 'sil' and ti[0] != 'noise':
        #     # f.write('SPEAKER' + ' ' + uri + ' ' + '1' + ' ' + str(round(start, 3)) + ' ' + str(ti[1]) + ' <NA> <NA> ' + ti[0] + ' <NA> <NA>' + '\n')
        #     end = start + ti[1]
        #     f.write(uri+ '_' + str(i) + ' ' + uri + ' ' + str(round(start, 3)) + ' ' + str(round(end, 3)) + '\n')
        #     start = start + ti[1]
        # else:
        #     start =
        #     end = start + ti[1]
        #     f.write(uri + '_' + str(i) + ' ' + uri + ' ' + str(round(start, 3)) + ' ' + str(round(end, 3)) + '\n')
        #     start = start + ti[1]
        #i += 1
f.close()


# 保存拼接音频
output = wave.open(outfile, 'wb')
output.setparams(data[0][0])
for i in range(len(data)):
    output.writeframes(data[i][1])
output.close()

