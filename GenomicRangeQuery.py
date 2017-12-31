from datetime import datetime
startTime = datetime.now()

def solution(S,P,Q):
    if not(1<=len(S)<=10**5) or (len(P)!=len(Q)) or not(1<=len(P)<=50000):
        return -1
    s0=[None]*len(S)
    for i in range(len(S)):
        ci=S[i]
        if ci=="A":
            s0[i]=0
        elif ci=="C":
            s0[i]=1
        elif ci=="G":
            s0[i]=2
        elif ci=="T":
            s0[i]=3
        else: return -1
    
    s1=[[0,0,0,0]for y in range(len(S)+1)]
    
    
    for i in range(1,len(S)+1):
        for j in range(4):
            s1[i][j]=s1[i-1][j]
        s1[i][s0[i-1]]+=1
    
    res=[]
    for i in range(len(P)):
        for j in range(4):
            lbound=P[i]
            ubound=Q[i]+1
            if ubound<lbound: return -1
            if s1[lbound][j]!=s1[ubound][j]:
                res.append(j+1)
                break
            #print(i,j,lbound,s1[lbound][j],ubound,s1[ubound][j])
    return res


S="CAGCCTA"
P=[2,5,0]
Q=[4,5,6]
b=solution(S,P,Q)
print(b)

print (datetime.now() - startTime)