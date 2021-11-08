import soundfile as sf
import os
import numpy as np


def left_right(audio_path, name):
    '''
    保留左声道或者右声道
    :param audio_path:
    :return:
    '''
    lname = 'l' + name
    rname = 'r' + name
    # 保存路径
    path = 'F:\\20210823语料\\哈尔滨\\'
    l_path = os.path.join(path, lname)
    r_path = os.path.join(path, rname)
    # 读取音频
    data, sr1 = sf.read(audio_path, dtype=np.int16)
    # 保存音频
    sf.write(l_path, data[:, 0], samplerate=8000)
    sf.write(r_path, data[:, 1], samplerate=8000)


if __name__ == '__main__':
    path = 'F:\\20210823语料\\哈尔滨\\20210821151018_Q_101023_1011_018689767787.wav'
    name = path.strip().split('\\')[-1]
    left_right(path, name)