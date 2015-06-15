def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

k= str(fact(100))
sum=0
for i in k:
    sum+=int(i)

print sum
