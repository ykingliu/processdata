"""Python绘制语谱图"""
"""Python绘制时域波形"""

# 导入相应的包
import numpy, wave
import matplotlib.pyplot as plt
import numpy as np
import os

filepath = 'E:\\数据集\\噪声\\merge\\例子\\1\\'  # 添加路径
filename = os.listdir(filepath)  # 得到文件夹下的所有文件名

for i in range(len(filename)):
    f = wave.open(filepath + filename[i], 'rb')  # 调用wave模块中的open函数，打开语音文件。
    params = f.getparams()  # 得到语音参数
    nchannels, sampwidth, framerate, nframes = params[:4]  # nchannels:音频通道数，sampwidth:每个音频样本的字节数，framerate:采样率，nframes:音频采样点数
    strData = f.readframes(nframes)  # 读取音频，字符串格式
    wavaData = np.fromstring(strData, dtype=np.int16)  # 得到的数据是字符串，将字符串转为int型
    wavaData = wavaData * 1.0/max(abs(wavaData))  # wave幅值归一化
    wavaData = np.reshape(wavaData, [nframes, nchannels]).T  # .T 表示转置
    f.close()

    #（1）绘制语谱图
    plt.figure()
    plt.specgram(wavaData[0], Fs=framerate, scale_by_freq=True, sides='default')  # 绘制频谱
    plt.xlabel('Time(s)')
    plt.ylabel('Frequency')
    plt.title("Spectrogram_{}".format(i+1))
    plt.savefig('E:/数据集/噪声/merge/例子/1/音频图形/{}.jpg'.format(filename[i][:-4]))
    plt.show()

    #（2）绘制时域波形
    time = np.arange(0, nframes) * (1.0 / framerate)
    time = np.reshape(time, [nframes, 1]).T
    plt.plot(time[0, :nframes], wavaData[0, :nframes], c="b")
    plt.xlabel("time(seconds)")
    plt.ylabel("amplitude")
    plt.title("Original wave")
    plt.savefig('E:/数据集/噪声/merge/例子/1/音频图形/{}_.jpg'.format(filename[i][:-4]))  # 保存绘制的图形
    plt.show()
