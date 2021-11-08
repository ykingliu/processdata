def Match_Address(data):
    import re
    PATTERN1 = r'([\u4e00-\u9fa5]{2,5}?(?:省|自治区|市)){0,1}([\u4e00-\u9fa5]{2,7}?(?:区|县|州)){0,1}([\u4e00-\u9fa5]{2,7}?(?:镇)){0,1}([\u4e00-\u9fa5]{2,7}?(?:村|街|街道)){0,1}([\d]{1,3}?(号)){0,1}'
    # \u4e00-\u9fa5 匹配任何中文
    # {2,5} 匹配2到5次
    # ? 前面可不匹配  对我看你登记的户籍地址是在黑龙江省绥化市海伦市额丰山乡丰山村二组现在这个地址还有人在居住吗
    # (?:pattern) 如industr(?:y|ies) 就是一个比 'industry|industries' 更简略的表达式。意思就是说括号里面的内容是一个整体是以y或者ies结尾的单词
    pattern = re.compile(PATTERN1)
    p1 = ''
    p2 = ''
    p3 = ''
    p4 = ''
    p5 = ''
    p6 = ''
    m = pattern.search(data)
    print(m)
    if not m:
        print('None')
    if m.lastindex >= 1:
        p1 = m.group(1)
    if m.lastindex >= 2:
        p2 = m.group(2)
    if m.lastindex >= 3:
        p3 = m.group(3)
    if m.lastindex >= 4:
        p4 = m.group(4)
    if m.lastindex >= 5:
        p5 = m.group(5)
    if m.lastindex >= 6:
        p6 = m.group(6)
    out = '%s|%s|%s|%s|%s|%s' % (p1, p2, p3, p4, p5, p6)
    return out
if __name__ =='__main__':
    data=str(input("请输入文本:"))
    out=Match_Address(data)
    print(out)