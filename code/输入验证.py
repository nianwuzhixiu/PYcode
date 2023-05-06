import pyinputplus as pyip

def addToTen(numb):
    numblist=list(numb)
    for i,digit in enumerate(numblist):
        numblist[i]=int(digit)
    if sum(numblist)!=10:
        raise Exception('输入数字和不为10！，输入值和为：%s' % (sum(numblist)))
    return int(numb)

response = pyip.inputCustom(addToTen)
