from datetime import datetime
startTime = datetime.now()

def solution(A,k):
    B=[None]*len(A)
    for i in range(len(A)):
        B[(i+k)+(-int((i+k)/len(A))*len(A))]=A[i]
    return B

A=[1,2,3,4,5]
n=100.1
b=solution(A,int(n))
print(b)

print (datetime.now() - startTime)