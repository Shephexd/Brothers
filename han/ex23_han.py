def checkFactor(n):
    k=n
    i=2
    group=[1]
    while i<k/i:
        if(k%i==0):
            n=n/i
            group.append(i)
            group.append(k/i)
        i+=1
        
    if(i==k/i and k%i==0):
        group.append(i)
    
    return sum(group)

sumA,i=0,1
array,exceedNum=[],[]

while i<28123:
    
    if(i<checkFactor(i)):
        array.append(i)   
    i+=1

for x in array:
    for y in array:
        z=x+y
        if z<28123:
            exceedNum.append(x+y)

df= sum(range(1,28123))
re=sum(set(exceedNum))
print df-re,df,re
