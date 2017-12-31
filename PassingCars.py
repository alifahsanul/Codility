from datetime import datetime
startTime = datetime.now()


def solution(A):
    lenA=len(A)
    if not(1<=lenA<=10**5):
        return -1
    c0=A.count(0)
    c1=A.count(1)
    if c0+c1!=lenA:
        return -1
    t0=c0
    t1=c1
    passed=0
    for i in range(lenA):
        if A[i]==0:
            t0=t0-1
            passed += t1
        else:
            t1=t1-1
        if t1==0:
            break
    if passed>10**9:
        return -1
    return passed

A=[0,1,1,1,0,0,1,0]
#A=[0,0,0,0]
b=solution(A)
print(b)

print (datetime.now() - startTime)