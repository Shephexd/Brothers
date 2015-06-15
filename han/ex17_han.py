#one, two, six, ten count=3
#four,five,nine count=4
#three, seven,eight count=5

numOne = ["one","two","three","four","five","six","seven","eight","nine"]
numTenByTwenty = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
numTenPos = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]


def CheckNum(i):
    j=i-1
    if i<10:
        num = numOne[j]
        
    elif i<20:
        num = numTenByTwenty[j-9]

    elif i<100:#20이상 100이하 값
        k=i/10
        num = numTenPos[k-2]

        a=i%10
        if(a!=0):
            num += numOne[a-1]
            
    elif i<1000:
        m=i/100
        x=i%100
        
        num = numOne[m-1]
        num += "hundred"

        if(x!=0):
            num+="and"+CheckNum(x)
    elif i==1000:
        num = "onethousand"
    
    return num

count=0

for i in range(1,1001):#i는 숫자 j는 배열 맞추는 값
    n=CheckNum(i)
        
    
    count+=len(n)
    print count,len(n),i,n
