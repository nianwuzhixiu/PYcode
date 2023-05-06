import sys
def isValidChessBoard(chessBoard):
    for k,v in chessBoard.items():
        if int(k[:1])>10 and int(k[:1])<0:
            print(k[:1])
            return False
        if k[1:] not in ['a','b','c','d','e','f','g','h'] :
            print(k[1:])
            return False
        if v[:1] not in ['w','b'] :
            print(v[:1])
            return False
        if v[1:] not in ['pawn','knight','bishop','rook','queen','king'] :
            print(v[1:])
            return False
        return True

chessBoard={}
while 1==1:
    print('输入地址下棋：')
    addresschess=input()
    print('输入驱动的棋子：')
    chessuse=input()
    chessBoard[addresschess]=chessuse
    isok=isValidChessBoard(chessBoard)
    print(isok)
    print(chessBoard)
    if isok :
        print('棋盘正确!')
    else:
        print('棋盘不正确！')
    print('是否退出？（Y/N）')
    yon=input().upper()
    if yon=='Y':
        break
sys.exit()
