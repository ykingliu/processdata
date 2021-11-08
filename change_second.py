from pydub import AudioSegment
import random
import glob
# 创建1s的静音

# 噪声片段
noise_seg = glob.glob('F:\\分割聚类\\收集噪声\\*.wav')
print(noise_seg)

for i in range(10):
    a = random.randint(0,2)
    #print(a)
    one_sec_segment = AudioSegment.silent(duration=(a * 1000)).set_frame_rate(8000)
    one_sec_segment = one_sec_segment.raw_data
    #print(one_sec_segment)
    b = random.randint(0,4) # 随机噪声参数
    print(b)
    print(noise_seg[b])


