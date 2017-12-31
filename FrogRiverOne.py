from datetime import datetime
startTime = datetime.now()

def solution(X, A):
    lenA=len(A)
    if lenA<1 or lenA>10**5 or X<1 or X>10**5:
        return -1
    maxA=max(A)
    minA=min(A)
    if maxA>X or minA<1:
        return -1
    storage=[False]*X
    for i in range(lenA):
        if storage[A[i]-1]==False:
            storage[A[i]-1]=True
            X=X-1
    return X


a=45000
A=list(range(1,a+1))
X=a
b=solution(X,A)
print(b)

print (datetime.now() - startTime)