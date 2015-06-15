import math

target=100
sum=0

for i in range(2,target):
    for k in range(2,int(math.sqrt(i))+1 ):
        print i,k
        if(i%k==0):
            i=0
            break

    sum=sum+i

print sum
