# code=utf-8
import pandas as pd


# 打开文件
data = pd.read_csv('./audio_info-10.csv')
print(data.shape)


# 每个excel保存3万行，那么530000+数据需要18个.csv文档保存
for i in range(0, 5):
    save_data = data.iloc[i*6000 + 1 : (i+1)*6000+1]
    file_name = 'audio_info-10-' + str(i) + '.csv'  # 保存文件路径以及文件名称
    print(file_name)
    save_data.to_csv(file_name, index=False)  # 保存格式为.csv，如果是xlsx则修改为save_data.to_excel

'''
data = pd.read_csv('./audio_info-9-3.csv')
print(data.shape)
'''