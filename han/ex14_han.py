
best = 0
bestN=0
k=0
for n in range(1,1000000):
    count=0
    
    while n!=1:
        if(n%2==0):
            n/=2
        else:
            n=3*n+1
        count+=1
        
    if(count>best):
        best=count
        bestN=k
        
print best,k,bestN
