from datetime import datetime
startTime = datetime.now()

def solution(A):
    lenA=len(A)
    if not(3<=lenA<=10**5): return -1
    A.sort()
    if max(A)>1000 or min(A)<-1000: return -1
    
    bigval=A[0]*A[1]
    currentmax=A[-1]*A[-2]*A[-3]
    for i in range(2,lenA):
        checkval=bigval*A[i]
        if checkval>currentmax:
            currentmax=checkval
    bigval=A[-1]*A[-2]
    for i in range(0,lenA-2):
        checkval=bigval*A[i]
        if checkval>currentmax:
            currentmax=checkval
    return currentmax


A=[2,-6,1,3,-5,3,2,5]
A=[-3,-2,0]
#A=[]
#A=[-10**6,10**6+1]
#A=[-10**6-0]*10**5
#A=[10**6+0]*10**5
#A=[0,0]
#A=[-1]
#A=[3]
#A=[[1,2],[3,5]]
A=[0,0,0]
A=[-2,-2,-2]
A=[-2,1,2]
A=[3,3,4,6,1,0]
A=[3,4,1]
A=[-1,-1,-1]
A=[4, 7, 3, 2, 1, -3, -5]

b=solution(A)
print(b)

print (datetime.now() - startTime)