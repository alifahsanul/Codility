from datetime import datetime
startTime = datetime.now()

def solution(A):
    if not(2<=len(A)<=10**5):return -1
    if max(A)>10**4 or min(A)<-10**4: return -1
    if (len(A))==2: return 0
    res=0
    minave=(A[0]+A[1])*0.5
    for i in range(len(A)-2):
        if minave>((A[i]+A[i+1])/2):
            minave=(A[i]+A[i+1])/2
            #print("a",i,minave)
            res=i
        if minave> ((A[i]+A[i+1]+A[i+2])/3):
            minave =((A[i]+A[i+1]+A[i+2])/3)
            #print("b",i,minave)
            res=i
    i+=1
    #print("d",i,minave)
    if minave>((A[i]+A[i+1])/2):
        minave=(A[i]+A[i+1])/2
        res=i
        #print("c",i,minave)
    return res



A=[2,6]
b=solution(A)
print(b)

print (datetime.now() - startTime)