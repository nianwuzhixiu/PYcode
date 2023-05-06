#一个多剪贴板程序。py3

TEXT = {'同意': """我同意这个说法。""",
        '忙碌': """对不起我比较忙，下周再说。""",
        '存钱': """你这个月存钱吗?"""}

import sys, pyperclip
if len(sys.argv) < 2:
    print('输入方式: py mclip.py [keyphrase] - 复制短语文')
    sys.exit()

keyphrase = sys.argv[1]    # 第一个命令行arg是TEXT中的keyphraseif关键短语
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)
