from datetime import datetime
startTime = datetime.now()

def solution(A):
    lenA=len(A)
    if lenA<1 or lenA>10**5:
        return -1
    if max(A)>10**9 or min(A)<1:
        return -1
    ch1=0
    for i in range(lenA):
        ch1=ch1^A[i]^(i+1)
        #print(i+1,A[i],ch1)
    if ch1==0:
        return 1
    else:
        return 0

A=[99999999999,-9999999999999999,2]
A=[]
A=[10**9]*(10**5)
A=[3,2,1,4,6,5,9,11999]
b=solution(A)
print(b)

print (datetime.now() - startTime)