#! python3
# phoneAndEmail.py - 在剪贴板上查找电话号码和电子邮件地址.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?      #地区
    (\s|-|\.)?               #连接符
    (\d{4})                 #前三位
    (\s|-|\.)               #连接符
    (\d{4})                 #中间四位
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # 分机
    )''', re.VERBOSE)
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # 名字
    @                       # @
    [a-zA-Z0-9.-]+          # 域名
    (\.[a-zA-Z]{2,4})      # dot-something
    )''', re.VERBOSE)

# 在剪贴板文本中查找匹配项。
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('复制到剪贴板:')
    print('\n'.join(matches))
else:
    print('没找到电话和邮箱.')

