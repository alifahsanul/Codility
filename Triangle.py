from datetime import datetime
startTime = datetime.now()

def solution(A):
    if not(3<=len(A)<=10**5): return -1
    if len(A)<3: return 0
    A.sort()
    flag=0
    b=2147483647
    for i in range(len(A)-2):
        if not(-b<=A[i]<=b) or not(-b<=A[i+1]<=b) or not(-b<=A[i+2]<=b): return 0
        if A[i]+A[i+1]>A[i+2]:
            flag=flag+1
    if flag>0: return 1
    else: return 0


A=[2,6]
b=solution(A)
print(b)

print (datetime.now() - startTime)