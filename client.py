import requests
import os
from multiprocessing import Pool, Process
import time
import soundfile as sf
from scipy.io import wavfile

def post(path):
    url = "http://172.16.1.68:8008/diarization"
    name = path.strip().split("/")[-1].replace('.wav', '')
    rate, data1 = wavfile.read(path)
    print(data1)
    print(type(data1))
    data2, samplerate = sf.read(path)
    print(data2)
    print(type(data2))
    
    para = {'name': name, 'format': 'pcm', 'sample_rate': rate, 'data1': data1.tolist(), 'data2': data2.tolist()}
    result = requests.post(url, json=para)
    return result.text

if __name__ == '__main__':
    audio_path = 'C:\\Users\\liuyuanqing\\Downloads\\476.wav'
    pred = post(audio_path)
    print(pred)
    
    
    
    