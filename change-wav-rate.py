import librosa
import os
import glob

def resample_rate(path,new_sample_rate = 8000):
    out_path = 'F:\\20210610语音识别新语料\\new_audio\\问题音频\\change\\'
    signal, sr = librosa.load(path, sr=None)
    wavfile = path.split('/')[-1]
    wav_name = path.strip().split('\\')[-1]
    print(wav_name)
    wavfile = wavfile.split('.')[0]
    file_name = wavfile + '.wav'
    file_path = os.path.join(out_path, wav_name)
    print(file_path)
    new_signal = librosa.resample(signal, sr, new_sample_rate) #
    librosa.output.write_wav(file_path, new_signal , new_sample_rate)

path = 'F:\\20210610语音识别新语料\\new_audio\\track2\\20210513134547-13471088099本人.mp3'
for i in glob.glob('F:\\20210610语音识别新语料\\new_audio\\问题音频\\' + '/*'):
    resample_rate(i)
