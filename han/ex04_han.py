# -*- coding: utf-8 -*-

def PalinSort(c,num):
    palin=[]
    for i in range(1,num):
        x=c%10
        c=int(c/10)
        palin.append(x)

    return palin

def CheckPalin(pa,num):
    i=0
    result = False
    while i<num/2:
        if pa[-(1+i)]!=pa[i]:
            result=False
            break

        result=True
        i=i+1

    if result:
        return pa

a=0
b=999
start=999
stop=900
ch=False

for b in range(start,stop,-1):
    for a in range(b,900,-1):
        c=a*b
        pa = PalinSort(c,7)
        res=CheckPalin(pa,7)
        if res:
            print res,a,b

