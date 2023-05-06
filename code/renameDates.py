#! python3
# renameDates.py - 重新命名日期格式
# to European YYYY-DD-MM.

import shutil,os,re
from pathlib import Path
#创建一个筛选日期的正则表达式
datePattern=re.compile(r"""^(.*?)   #日期前任何文本
    ((19|20)\d\d)
    ((0|1)\d)
    ((0|1|2|3)\d)                   #匹配第一次日期格式年月日8位
    (.*?)$                          #匹配任意文本结束
    """,re.VERBOSE)

#获取文件名
fl=Path('D:\\PYCODE\\cs')
for filesName   in os.listdir(fl):
    mo=datePattern.findall(filesName)
    print(filesName)
    if mo==None:
        continue
    #获取年月日字符串
    for result in mo:
        beforePart = result[0]
        yearPart = result[1]
        monthPart = result[3]
        dayPart = result[5]
        afterPart = result[7]
        euroFilename=beforePart+yearPart+'-'+monthPart+'-'+dayPart+afterPart
        print(f'{filesName}重命名为{euroFilename}')
        shutil.move(fl/filesName,fl/euroFilename)


