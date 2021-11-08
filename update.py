import pymysql
import json

# 连接database
mysqlConn = pymysql.connect(host='172.16.1.140', user='woaixgs',password='lianxin',database='woaixgs',charset='utf8')
# 得到一个可以执行SQL语句的光标对象
cursor = mysqlConn.cursor()
# 定义要执行的SQL语句
sql = """
select * from entity_poetry;
"""
# 执行SQL语句
cursor.execute(sql)

#处理
result = cursor.fetchall()
for poetry in result:
    poetryUID = poetry[1]
    partInfo = poetry[19]
    print(partInfo)

    # name
    partInfo = json.load(partInfo)
    name = partInfo["name"]
    if name is not None:
        nameRemind = {"talk_uid": name["audio"], "reference_img": ""}
        nameRemindList = [nameRemind]
        name["remindList"] = nameRemindList
        del name["audio"]

    # dynasty
    dynasty = partInfo["dynasty"]
    if dynasty is not None and dynasty != '':
        dynastyRemind = {"talk_uid": dynasty["audio"], "reference_img": ""}
        dynastyRemindList = [dynastyRemind]
        dynasty["remindList"] = dynastyRemindList
        del dynasty["audio"]

    # author
    author = partInfo["author"]
    if author is not None and author != '':
        authorRemind = {"talk_uid": author["audio"], "reference_img": ""}
        authorRemindList = [authorRemind]
        author["remindList"] = authorRemindList
        del author["audio"]

    # connect
    connectList = partInfo["connect"]
    for connect in connectList:
        textList = connect["text"]
        for text in textList:
            textRemind = {"talk_uid": text["audio"], "reference_img": ""}
            textRemindList = [textRemind]
            text["remindList"] = authorRemindList
            del text["audio"]
print(partInfo)


# 关闭光标对象
cursor.close()
# 关闭数据库连接
mysqlConn.close()
