fiba=[1,1]
i=3
while True:
    x=fiba[-2]+fiba[-1]
    fiba.append(x)
    if(len(str(fiba[-1])))==1000:
        break
    
    i+=1

print i,fiba[-1]
