import math

count=2
target=2
result = False

while count<10001:
    for x in range(2,int(math.sqrt(target))+1):
        if(target%x==0):
            result = False
            break
        result = True
        
    if(result):
        count=count+1
        
    target+=1
print target
