import os
from pathlib import  Path


# 要删除的文件路径

filep=Path.cwd()
contdel=0
try:
    # 删除文件
    for file in filep.glob('*.docx'):
        os.remove(file)
        print(f"文件 {file} 已删除")
        contdel+=1
    print(f'共删除{contdel}个文件')
except OSError as error:
    print(f"删除文件时出错: {error}")
