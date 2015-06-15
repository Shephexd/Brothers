res1,res2=float(),float()

s1,s2=1.0,1.0
for n1 in range(10,100):
    for n2 in range(10,n1):
        a,b=str(n2),str(n1)
        c,d=float(),float()

        
        if(a[0]==b[0]):
            c,d=float(a[1]),float(b[1])

        elif(a[0]==b[1]):        
            c,d=float(a[1]),float(b[0])    

        elif(a[1]==b[0]):
            c,d=float(a[0]),float(b[1])

        elif(a[1]==b[1] and a[1]!='0'):        
            c,d=float(a[0]),float(b[0])    

        else:
            a,b,c,d=0,0,0,0
        if(float(d)!=0 and float(c)<float(d)):
            res1,res2= float(a)/float(b),float(c)/float(d)

            if(res1==res2):
                s1*=c
                s2*=d
                print a,b,res1,res2,s1/s2
                
