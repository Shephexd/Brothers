f=open("ex22_data.txt","r")
k= f.readline()

i=1
score=0
result=0
j=k.split(",")

j=sorted(j)
for s in j:
    sumA=0
    temp=""
    for c in s:
        if(c>="A" and c<="Z"):
            sumA+=ord(c)-64
            
    score=sumA*i
    result+=score
    i+=1

print result
