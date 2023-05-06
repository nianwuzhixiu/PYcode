import logging
logging.basicConfig(filename='myProgramLog.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)
spam=10
assert spam>=10,'spam小于10！'
sta='helloo'
stb='HellO'
assert sta.lower()!=stb.lower(),'两个字符串相等！'

assert 1==1,'总是错误！'

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)'  % (n))
    total  =   1
    for i in range(1,n + 1):
        total *= i
        logging.debug('i is ' +  str(i) +  ', total is ' +  str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')
