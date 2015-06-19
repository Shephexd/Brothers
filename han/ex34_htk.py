def factor(n):
    if n==1:
        return 1

    if n==0:
        return 0

    elif n>0:
        return n*factor(n-1)
    

facList=[1,]

for x in range(1,10):
    facList.append(factor(x))

print facList

result=0
n=3

while 1:
    sumN=0

    for i in str(n):

        sumN+=facList[int(i)]

        
        if(sumN>n):
            break
    
    if(sumN==int(n)):
        
        result+=n
        print result,n
    n+=1
