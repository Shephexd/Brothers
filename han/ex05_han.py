k=1
for i in range(2,21):
    print "---------------"  
    print k,i

    t=2
    while k%i!=0:
        k=k*t
        if(k%i!=0):
            k=k/t
        
        t=t+1
        
    print k,i

print k
