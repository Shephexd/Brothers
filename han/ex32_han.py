def CheckPan(n):
    target=str(n)
    if(target.count("0") or len(target)!=9):
        return False
    
    for x in range(1,10):
        if(target.count(str(x))>1):
            return False

    return True


a=39
b=186
c=a*b
li=list()
for a in range(1,5000):
    for b in range(1,99):
        c=a*b
        if(CheckPan(str(a)+str(b)+str(c))):
           li.append(c)
           print a,"*",b,"=",c
li=set(li)
print li
print sum(li)
