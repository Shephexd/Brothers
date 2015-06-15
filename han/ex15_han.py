course=['right','right','right',
        'right','right','right',
        'right','right','right',
        'right','right','right',
        'right','right','right',
        'right','right','right',
        'right','right',
        'down','down','down',
        'down','down','down',
        'down','down','down',
        'down','down','down',
        'down','down','down',
        'down','down','down',
        'down','down']
array = []
count= 0
error= 0
i=0
turn = 1
while error<38 or turn !=100000:
    check="-".join(course)
    
    if(not (check in array)):
        array.append(check)
        count+=1
        
    else:
        error+=1

    if(error==38):
        turn+=1
        
    if(i==39):
        error=0
        i=0

    temp=course[i]
    course[i]=course[i+1]
    course[i+1]=temp

    i+=1



print count,error,turn
