from datetime import datetime
startTime = datetime.now()

def solution(A):
    # write your code in Python 3.6
    lenA=len(A)
    if lenA>10**5 or lenA<1:
        return -1
    maxA=max(A)
    minA=min(A)
    
    if maxA<1:
        return 1
    
    if maxA>10**6 or minA<-10**6:
        return -1
    
    bool=[False]*(lenA)
    for i in range(lenA):
        if A[i]>0 and A[i]<len(A)+1:
            bool[A[i]-1]=True
    
    counter=0
    for i in range(len(bool)):
        if (bool[i])==False:
            return i+1
            counter = counter +1
    if counter==0:
        return i+2


a=10**5+0
A=list(range(1,a+1))
#A=[1,(-10**6)-1]
#A=[-0+10**6]
#A=[]

b=solution(A)
print(b)

print (datetime.now() - startTime)