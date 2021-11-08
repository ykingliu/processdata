import wave
import contextlib
import os
import time

# ============================统计音频时长=================================

t = time.time()
wav_dir = "F:\\分割聚类\\分割聚类测试\\测试\\20211011_30\\wavs\\"
# wav_dir = "F:\\20210706语料\\lar15s\\音频切割-98.15h\\"


total_time = 0
ii = 0
with open('contextlib_duration.txt', 'w', encoding='utf-8')as log:
	for file in os.listdir(wav_dir):
		ii += 1
		file_path = os.path.join(wav_dir, file)
		with contextlib.closing(wave.open(file_path, 'r')) as f:
			frames = f.getnframes()         # 帧数
			rate = f.getframerate()         # 帧率（每秒的帧数）
			duration = frames / float(rate) # 单位：秒
			total_time = total_time + duration
			content = file + " " + str(duration) + "\n"
			log.write(content)
print("wave num", ii)
print("total_time = ",total_time)
print("Effective hours: ", total_time/3600)
print(time.time() - t)

# =========================================================================

# text = '啊你好万家汇对吧范女士嗯嗯唉你好我这边给您这个兴业银行逾期案件的您这边不是有一张卡逾期挺长时间了哦我看了一下这个工作人员也跟您沟通过那您这边钱筹的咋样了喂'
# print(text.count('先生'))
# print(text.count('女士'))
# print(text.count('您'))
# w = text.count('先生') + text.count('女士') + text.count('您')
# print(w)

# =======================统计聚类后的每各类的总时长=============================
# l, m, n = 0, 0, 0
# s1, s2, s3 = 0, 0, 0
#
# fh = open('E:\\工作目标\\2021\\202107演示材料\\情绪\\8011_13901114265_20210111_155656-1.txt', 'r')
# for line in fh.readlines():
# 	start = line.strip().split('\t')[0]
# 	end = line.strip().split('\t')[1]
# 	duration = float(end) - float(start)
# 	label = line.strip().split('\t')[2]
# 	if label == '1':
# 		l += 1
# 		s1 += duration
# 	if label == '2':
# 		m += 1
# 		s2 += duration
# 	if label == '3':
# 		n += 1
# 		s3 += duration
# print(l)
# print(s1)
# print(m)
# print(s2)
# print(n)
# print(s3)
