import random,sys
succesnumb=random.randint(1,100)
print('猜一个数，它在1~100之间。')

for guessnumb in range(1,10):
    guess=int(input())
    if guess>succesnumb:
        print('数字猜大了，重新猜！')
    elif guess<succesnumb:
        print('数字猜小了，重新猜！')
    else:
        print('猜对了！数字是'+str(guess)+'。')
        sys.exit()
        break

print('猜测次数用完，猜数字失败！')
#
