from datetime import datetime
startTime = datetime.now()


def solution(N, A):
    arrayN=[0]*N
    maxtemp=0
    lastupdate=0
    for Ai in A:
        if 1<=Ai<=N:
            if arrayN[Ai-1]<lastupdate:
                arrayN[Ai-1]=lastupdate
            arrayN[Ai-1] += 1
            if arrayN[Ai-1]>maxtemp:
                maxtemp=arrayN[Ai-1]
        else:
            lastupdate=maxtemp
    for i in range(len(arrayN)):
        if arrayN[i]<lastupdate:
            arrayN[i]=lastupdate
    return arrayN


a=10**5
A=list(range(1,a+1))
A[-4]=a
N=a
A=[1,1,4,1,4,1]
N=3

#A=[1,(-10**6)-1]
#A=[-0+10**6]
#A=[]

b=solution(N,A)
print(b)

print (datetime.now() - startTime)