import math

def CheckP(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
        
result=list()
maxcount=0
for a in range(-999,1000):
    for b in range(-999,1000):
        
        n,count=0,0
        while n<=abs(a):
            formula=(n*n+a*n+b)
            
            if CheckP(abs(formula)):
                count+=1
            else:
                break
            n+=1
        if(count>maxcount):
            maxcount=count
            print a,b,n,count,formula

print maxcount
