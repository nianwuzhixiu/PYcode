import time,sys

times=0
ifpass=True

try:
    while True:
        print(' ' * times,end='')
        print('**********')
        time.sleep(0.1)
        if ifpass:
            times=times+1
            if times>=20:
                ifpass=False
        else:
            times=times-1
            if times<=0:
                ifpass=True

except KeyboardInterrupt:
   sys.exit()

