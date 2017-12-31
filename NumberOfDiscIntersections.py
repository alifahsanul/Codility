from datetime import datetime
startTime = datetime.now()

def solution(A):
    lenA=len(A)
    if not(0<=lenA<=10**5): return -1
    timeline=[]
    for i in range(lenA):
        if not(0<=A[i]<=2147483647): return -1
        timeline+=[(i-A[i],True),(i+A[i],False)]
    timeline.sort(key=lambda x: (x[0],-x[1]))
    intersect=0
    currentcircle=0
    for i in range(lenA*2):
        if timeline[i][1]:
            intersect+=currentcircle
            currentcircle+=1
        else:
            currentcircle-=1
    if intersect>10**7: return -1
    return intersect

A=[1,2,3,0]
b=solution(A)
print(b)
print (datetime.now() - startTime)