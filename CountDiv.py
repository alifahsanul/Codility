from datetime import datetime
startTime = datetime.now()


def solution(A, B, K):
    bound=2*10**6
    if A<0 or A>bound or B<0 or B>bound or K<1 or K>bound or A>B:
        return -1
    c=0
    if A%K==0:
        c=1
    a=int(A/K)
    b=int(B/K)
    d=b-a+c
    return d

b=solution(1,5,2)
print(b)

print (datetime.now() - startTime)