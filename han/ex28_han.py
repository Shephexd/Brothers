xpos=0
ypos=0

start=0

spiralSum=1
num=1
a=1
b=1
while abs(xpos)<=500 and abs(ypos)<=500:
    
    xpos+=a
    ypos+=b
    
    num+=(abs(a)+abs(b))
    if(abs(xpos)==abs(ypos)):
        spiralSum+=num
        if(xpos>start and ypos>start):
            a=-1
            b=0
        if(xpos<start and ypos>start):
            a=0
            b=-1
        if(xpos<start and ypos<start):
            a=1
            b=0
        if(xpos>start and ypos<start):
            a=0
            b=1
            num+=1
            xpos+=1
            
print spiralSum,num
