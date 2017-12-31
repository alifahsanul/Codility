from datetime import datetime
startTime = datetime.now()

def solution(A):
    if len(A)%2==0 or len(A)<1 or len(A)>1000000 or max(A)>1000000000 or min(A)<1:
        return -1
    
    i=0
    result=0
    while i<len(A):
        result = result ^ A[i]
        i=i+1
    return result

A=[99999999999,-9999999999999999,2]
b=solution(A)
print(b)

print (datetime.now() - startTime)