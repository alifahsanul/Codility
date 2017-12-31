# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    
    max_gap=0
    current_gap=0
    
    if not(isinstance(N,int)) or N<0 or N>2147483647:
        raise ValueError ("Must be positive integer less or equal than 2147483647")
        return -1
    
    b="{0:b}".format(N)
    
    if b[0]!="1":
        return -1
    
    for i in range(len(b)):
        if b[i]=="0":
            current_gap=current_gap+1
        else:
            if current_gap>max_gap:
                max_gap=current_gap
            current_gap=0
    return max_gap

a=2147483647
#print("{0:b}".format(a))
b=solution(a)
print("aaaa",b)

