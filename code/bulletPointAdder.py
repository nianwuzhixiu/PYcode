#! python3
# bulletPointAdder.py - 将维基百科的要点添加到开头
# 剪贴板上的每一行文本

import pyperclip
text = pyperclip.paste()

# TODO: 剪贴板上的每一行文本.
text=text.split('\n')
for i in range(len(text)):
    text[i]='* '+text[i]

text='\n'.join(text)

pyperclip.copy(text)
