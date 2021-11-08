import glob
import wave
import random
from pydub import AudioSegment

outfile = "C:\\Users\\liuyuanqing\\Desktop\\验证\\情绪测试音频\\emotion.wav"
audio_seg = glob.glob('C:\\Users\\liuyuanqing\\Desktop\\验证\\情绪测试音频\\各种情绪\\*.wav')

data = []
time = []
for seg in audio_seg:
    w = wave.open(seg, 'rb')
    fr = w.getframerate()
    nf = w.getnframes()
    length = round((float(nf) / float(fr)), 5)
    print(length)
    name = seg.strip().split('\\')[-1]
    # 各个音频片段的间隔
    time.append([name, length])
    data.append([w.getparams(), w.readframes(w.getnframes())])
    i = 0  # 停止随机直接进行插入静音
    if i == 0:
        # a = random.randint(1, 3)  # 随机生成静音参数
        a = 2 #直接定义加入静音为2s
        # 产生对应的静音bytes
        one_sec_segment = AudioSegment.silent(duration=(a * 1000)).set_frame_rate(8000)
        one_sec_segment = one_sec_segment.raw_data
        data.append([w.getparams(), one_sec_segment])
        time.append(['sil', a])
    w.close()

k = 0
start = 0.0
uri = outfile.strip().split('\\')[-1].replace('.wav', '')
with open(outfile.replace('.wav', '.txt'), 'w', encoding='utf-8') as f:
    for ti in time:
        if ti[0] != 'sil' and ti[0] != 'noise':
            f.write(str(round(start, 3)) + '\t' + str(round(start, 3) + ti[1]) + '\t' +'sp' + '\n')
            start = start + ti[1]
        else:
            start = start + ti[1]
f.close()

# 保存拼接音频
output = wave.open(outfile, 'wb')
output.setparams(data[0][0])
for i in range(len(data)):
    output.writeframes(data[i][1])
output.close()