import sys,random

print('欢迎来玩石头、剪刀、布！')
win=0
loss=0
draw=0

while True :
    print('赢 %s     输 %s    平 %s     ' % (win,loss,draw))
    while True:
        print('输入剪刀（j）石头（s）布（b） 退出（q）：')
        gamer=input()
        if gamer!='j' and gamer!='s' and gamer!='b':
            print('输入错误重新输入！')
            continue
        if gamer=='q':
            print('游戏结束！')
            sys.exit()
        break
    if gamer=='j':
        print('玩家出了剪刀！')
    elif gamer=='s':
        print('玩家出了石头！')
    elif gamer=='b':
        print('玩家出了布！')
    numb=random.randint(1,3)
    if numb==1:
        npc='j'
        print('电脑出了剪刀！')
    elif numb==2:
        npc='s'
        print('电脑出了石头!')
    elif numb==3:
        npc='b'
        print('电脑出了布！')
    if gamer==npc:
        draw=draw+1
        print('平手！')
        continue
    elif gamer=='j' and npc=='b':
        win=win+1
        print('你赢了！')
        continue
    elif gamer=='s' and npc=='j':
        win=win+1
        print('你赢了！')
        continue
    elif gamer=='b' and npc=='s':
        win=win+1
        print('你赢了！')
        continue
    else :
        loss=loss+1
        print('你输了！')
        continue




