#! python3
# mapIt.py - 使用命令行或剪贴板中的地址在浏览器中启动网址。

import webbrowser, sys, pyperclip

try:
    # 获取地址
    if len(sys.argv)  >  1:     # 从命令行获取地址。
        address  =  ' '.join(sys.argv[1:])
    else:                        # 从粘贴板获取地址
        address = pyperclip.paste()
    if not address:
        raise ValueError('地址为空!')  # 抛出异常
except ValueError as err:
    print(err)                      # 地址为空!
else:
    webbrowser.open(
"https://search.bilibili.com/all?keyword="+address
)
