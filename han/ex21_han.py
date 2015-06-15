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

sumA=0
i=2


while i<10000:
    x=checkFactor(i)
    y=checkFactor(x)

    if(i==y and x!=i):
        sumA+=i
    i+=1
    
print i,sumA
