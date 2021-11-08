import pandas as pd
'''
#提取字符数量大于四的音频信息
reader = pd.read_csv('./10.csv')
reader["num"] = reader["audio_text"].str.len()
new = reader[reader["audio_text"].str.len()>4]
new_df = new["end_point"]-new["start_point"]
new["all_time"] = new_df
new_csv = new[new["all_time"]<=15]
new_csv1 = new_csv[new_csv["all_time"]>=7]
new_csv2 = new[new["all_time"]>15]

print(new.shape)
print(new_csv.shape)
print(new_csv1.shape)
print(new_csv2.shape)
#new_csv.to_csv('./10-lager4.csv')
new_csv1.to_csv('./10-lager7s.csv')
#new_csv2.to_csv('./10-lager15s.csv')
'''

reader = pd.read_csv('./8-lager7s.csv')
new = reader[reader["audio_info_id"]>=8545]
new_csv = new[new["audio_info_id"]<=8546]
print(new_csv.shape)
new_csv.to_csv('./8-khz.csv')

#########################################################
# 查找特定字符
# new = reader[reader["audio_text"].str.contains("，")]
# print(reader.shape)
# nw = reader[reader["audio_text"].isnull]
# print(nw.shape)

##########################################################
# reader = pd.read_csv('./audio_info (1).csv')
# new_a = reader[reader["create_time"]< "2020/8/3  11:01:39"]
# print(new_a.shape)
# new_df = reader["end_point"]-reader["start_point"]
# reader["all_time"] = new_df
# reader["text"] = reader["audio_text"].replace(", ", "")


#######################################################
'''
# 挑选
reader = pd.read_csv('./audio_info (1).csv')
new_csv = reader[reader["audio_info_id"] > 53799]
#new_csv1 = new_csv[new_csv["audio_info_id"]>21966]
new_csv.to_csv('./audio_info-10.csv')
print(new_csv.shape)
'''


# for i in range(20):
#    print(reader["text"].loc[i])
'''
for i in reader["audio_text"].loc[2]:
    r1 = i.replace(", ", "")
    reader["audio_text"] = r1
    #reader["text"]=reader["audio_text"].loc[i].replace(", ", "")
'''
'''
#特定字符替换
reader["audio_text"] = reader["audio_text"].str.replace(",", "")
reader["audio_text"] = reader["audio_text"].str.replace("，", "")
reader["audio_text"] = reader["audio_text"].str.replace("， ", "")
reader["audio_text"] = reader["audio_text"].str.replace("。", "")
#for i in range(10):
#    print(reader["audio_text"].loc[i])
reader.to_csv('./test-2.csv')
'''

# 统计时间
# print(reader["audio_text"].loc[1].replace(", ", ""))
# print(reader["all_time"].sum()/3600)
# 总的小时数：6236.507630555558
