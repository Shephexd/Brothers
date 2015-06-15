li=list()
for a in range(2,101):
    for b in range(2,101):
        k=a**b
        if not (k in li):
            li.append(k)

print len(li)
