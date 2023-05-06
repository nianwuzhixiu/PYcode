#multiplicationQuiz 乘法测试
import pyinputplus as pyip,random, time

nubOfQs=10
nibOfAs=0
for qsNub in range(nubOfQs):
    #生成两个随机数
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt='#%d , %d * %d = ' % (qsNub,num1,num2)
    try:
    # 正确答案由allowRegexes处理。
    # 错误的答案由blockRegexes处理，使用自定义消息。
        pyip.inputStr(prompt,allowRegexes=['^%s$' % (num1*num2)],
        blockRegexes=[('.*','错误!')],
        timeout=8,limit=3)
    except pyip.TimeoutException:
        print('超时！')
    except pyip.RetryLimitException:
        print('回答次数已用尽！')
    else:
        #回答正确，正确次数加一
        print('正确！')
        nibOfAs+=1
time.sleep(10)
print('正确率 = %d / %d' % (nibOfAs,nubOfQs))


