import random

numberOfTime=[]

for i in range(100000):
    if random.randint(0,1)==0:
        numberOfTime.append('A')
    else :
        numberOfTime.append('B')

count_a=0
count_b=0
a_get=0
b_get=0

for m in range(100000):
    if numberOfTime[m]=='A':
        count_a+=count_a
        count_b=0
    else:
        numberOfTime[m]=='B'
        count_b+=count_b
        count_a=0
    if count_a==2:
        a_get+=a_get
        count_a=0
    elif count_b==2:
        b_get+=b_get
        count_b=0

print('硬币连续出现六次正面的次数是%d，连续出现六次反面的次数是%d' % (a_get,b_get))
