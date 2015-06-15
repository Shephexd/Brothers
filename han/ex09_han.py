a = 1000
b = 0
c = 0
sol = 0
while 1:
    for a in range(1,500):
        c=1000-(a+b)

        if(a+b>c):
            if(a*a+b*b==c*c):
                sol = 1
                print a,b,c
                break
            
    if(sol):
        break
    b+=1

print a,b,c
print a*a+b*b
print c*c
print a*b*c
