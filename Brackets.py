from datetime import datetime
startTime = datetime.now()

def solution(S):
    # write your code in Python 3.6
    if not(0<=len(S)<=2*10**5): return -1
    opening=[]
    for sym in S:
        if sym not in ["(",")","[","]","{","}"]: return -1
        if sym=="(" or sym=="[" or sym=="{":
            opening.append(sym)
        else:
            if len(opening)==0:return 0
            first=opening.pop()
            if (sym==")" and first=="(") or (sym=="]" and first=="[") or (sym=="}" and first=="{"):
                pass
            else:
                return 0
    if len(opening)==0: return 1
    else: return 0

A="[][asda]"
A="[]"
b=solution(A)
print(b)
print (datetime.now() - startTime)