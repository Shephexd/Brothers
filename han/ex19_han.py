1,3,5,7,8,10,12
4,6,9,11
#mon=1,~sun=7

century=1901
month=1
day=1

half=7

dayCount=1
count=0

while century<2001:

    if(day==7):
        count+=1

    if(month==2):
        if(century%4==0 and century%400!=0 ):
            day+=1#29day
        else:
            pass#28day

    elif(month<=7):
        if(month%2==0):
            day+=2#30day
        elif(month%2==1):
            day+=3#31day
    else:
        if(month%2==0):
            day+=3#31day
        elif(month%2==1):
            day+=3#30day

    if(day>7):
        day=day%7



    
    month+=1
    if(month>12):
        month=month%12
        century+=1
        
    print century,month,count,day
