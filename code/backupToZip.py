#py3
#一键压缩文件夹，并批量添加递增的文件名
# 一个文件名递增的ZIP文件。

import zipfile, os

def backupToZip(folder):
    #将“文件夹”的全部内容备份为ZIP文件。
    folder  =  os.path.abspath(folder)    # 获取绝对路径
    print(folder)
    # 根据已经存在的文件找出该代码应该使用的文件名。
    number  =  1
    while True:     #循环添加zip文件名，如果文件存在number加一循环添加
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'#path.basename获取文件名
        if not os.path.exists(zipFilename): #找出是否存在文件
            break
        number  =  number  +  1
# TODO: 创建zip文件
    print(f'创建{zipFilename}')
    newzip=zipfile.ZipFile(zipFilename,'w')

# TODO: 遍历整个文件夹树并压缩每个文件夹中的文件。
    print('开始遍历文件树.')
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'添加{foldername}下的文件...')
        # 将当前文件夹添加到ZIP文件中。
        newzip.write(foldername)
        # 将此文件夹中的所有文件添加到ZIP文件中。
        for filename in filenames:
            newBase  =  os.path.basename(folder)  +  '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue    # 不要备份主文件夹开头ZIP文件
            newzip.write(os.path.join(foldername, filename))
    newzip.close()

backupToZip('D:\\PYCODE\\cs')
