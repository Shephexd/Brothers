import math

num=0
count=0
i=1

while count<500:
    count=0
    num+=i

    for x in range(1,int(math.sqrt(num)) ):
        if(num%x==0):
            count+=1
                
    count*=2        
    if(math.sqrt(num)-int(math.sqrt(num))==0 ):
        count+=1
    
    i+=1
            

print count,num,i
