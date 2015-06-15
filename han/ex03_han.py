import math

a = 600851475143

half = math.sqrt(a)
halfin =int(half)
group = []
realgroup =[]
print halfin

for num in range(1,halfin):
        if(a%num==0):
                group.append(num)
                print group

print group

result = 0
for num in group:
        k=int(math.sqrt(num))
        for x in range(2,k):
                if(num%x==0):
                        result=0
                        break
                else:
                        result=1

        if(result):
                realgroup.append(num)

print '--------------------------'
print realgroup
