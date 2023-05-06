import random,time,copy
WIDTH=10
HEIGHT=10

cells=[]
for x in range(WIDTH):
    column=[]
    for y in range(HEIGHT):
        if random.randint(0,1)==0:
            column.append('#')
        else:
            column.append(' ')
    cells.append(column)

nextcells=copy.deepcopy(cells)

while True:
    print('\n\n\n\n\n')

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(nextcells[x][y],end='|')
        print('')


    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord  = (x-1) % WIDTH
            rightCoord = (x+1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            lvlnum=0
            if nextcells[leftCoord][aboveCoord]=='#':
                lvlnum=lvlnum+1
            if nextcells[x][aboveCoord]=='#':
                lvlnum=lvlnum+1
            if nextcells[rightCoord][aboveCoord]=='#':
                lvlnum=lvlnum+1
            if nextcells[leftCoord][y]=='#':
                lvlnum=lvlnum+1
            if nextcells[rightCoord][y]=='#':
                lvlnum=lvlnum+1
            if nextcells[leftCoord][belowCoord]=='#':
                lvlnum=lvlnum+1
            if nextcells[x][belowCoord]=='#':
                lvlnum=lvlnum+1
            if nextcells[rightCoord][belowCoord]=='#':
                lvlnum=lvlnum+1

            if nextcells[x][y]=='#' and (lvlnum==2 or lvlnum==3):
                nextcells[x][y]='#'
            elif nextcells[x][y]==' ' and  lvlnum==3:
                nextcells[x][y]='#'
            else :
                nextcells[x][y]=' '
    time.sleep(5)

