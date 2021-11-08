import wave
import contextlib
import os
from shutil import move


wav_dir = "F:\\20210706语料\\lar15s\\音频切割\\"
out_dir = 'F:\\20210706语料\\lar15s\\丢弃\\'

for file in os.listdir(wav_dir):
    file_path = os.path.join(wav_dir, file)
    with contextlib.closing(wave.open(file_path, 'r')) as f:
        frames = f.getnframes()         # 帧数
        rate = f.getframerate()         # 帧率（每秒的帧数）
        duration = frames / float(rate) # 单位：秒
    f.close()
    if duration < 8:
        out = os.path.join(out_dir, file)
        move(file_path, out)