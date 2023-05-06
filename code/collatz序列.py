def collatz(x: int):
    if x % 2 == 0:
        x = x // 2

    elif x % 2 == 1:
        x = x * 3 + 1
    return x


try:
    print("输入一个数字：")
    numb = int(input())
    while numb != 1:
        numb = collatz(numb)
        print(numb)
except ValueError:
    print("输入正确的数字。")
