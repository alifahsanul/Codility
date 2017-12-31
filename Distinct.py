from datetime import datetime
startTime = datetime.now()

def solution(A):
    lenA=len(A)
    if not(0<=lenA<=10**5): return -1
    if lenA==0: return 0
    A.sort()
    B=[A[0]]
    print(B)
    for i in range(1,lenA):
        if not(-10**6<=A[i]<=10**6): return -1
        if A[i]!=B[-1]:
            B.append(A[i])
    lenB=len(B)
    return lenB


A=[2,6,1,3,5,3,2,5]
A=[]
#A=[-10**6,10**6+1]
#A=[-10**6-0]*10**5
#A=[10**6+0]*10**5
A=[0,0]
A=[-1]
A=[3]
A=[[1,2],[3,5]]
b=solution(A)
print(b)

print (datetime.now() - startTime)