result=list()
for num in range(2,300000):
    k=str(num)

    n=list()
    for x in k:
        n.append(int(x)**5)
      
    if(sum(n)==num):
        result.append(num)

print result
