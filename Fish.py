from datetime import datetime
startTime = datetime.now()
#A=[1,2,3,2,5,1]
#B=[0,0,1,0,0,0]
#A=[0,1]
#B=[0,0]
A=[4,3,2,1,5]
B=[0,1,0,0,0]
survivals = 0
stack = []
 
for idx in range(len(A)):
    if B[idx] == 0:
        while len(stack) != 0:
            if stack[-1] > A[idx]:
                break
            else:
                stack.pop()
        else:
            survivals += 1
    else:
        stack.append(A[idx])
survivals += len(stack)
"""
lenA=len(A)
lenB=len(B)
#if lenA!=lenB or not(0<=lenA<=2*10**5): return -1
alive=0
for i in range(lenA):
    #if not (0<=A[i]<=10**9): return -1
    checkalive=1
    if B[i]==0:
        if i>=1:
            for j in range(i-1,-1,-1):
                if A[i]<A[j] and B[j]==1:
                    checkalive=0
                    break
    if B[i]==1:
        if i<lenA and i>=0:
            for j in range(i+1,lenA):
                if A[i]<A[j] and B[j]==0:
                    checkalive=0
                    break
    alive+=checkalive
"""
"""
def solution(A,B):
    lenA=len(A)
    lenB=len(B)
    if lenA!=lenB or not(0<=lenA<=2*10**5): return -1
    alive=0
    dead=[]
    for i in range(lenA):
        if A[i]in dead: continue
        if not (0<=A[i]<=10**9): return -1
        checkalive=1
        if B[i]==0:
            if i!=0:
                for j in range(i-1,0,-1):
                    if A[i]<A[j]:
                        checkalive=0
                        dead.append(A[i])
                        break
        if B[i]==1:
            if i<lenA:
                for j in range(i+1,lenA):
                    if A[i]<A[j]:
                        checkalive=0
                        dead.append(A[i])
                        break
        alive+=checkalive
    return alive
"""
A="[][asda]"
A="[]"
#b=solution(A)
#print(b)
print (datetime.now() - startTime)