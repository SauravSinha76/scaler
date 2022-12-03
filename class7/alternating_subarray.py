def goodArr(A):
    n = len(A)
    for i in range(1,n):
        if A[i] == A[i-1]:
            return False
    return True

def solve(A,B):
    n = len(A)
    res = []
    for i in range(B,n-B):
        if goodArr(A[i-B:i+B+1]):
            res.append(i)
    return res

# A = [1, 0, 1, 0, 1]
# B = 1
# A = [0, 0, 0, 1, 1, 0, 1]
# B = 0
A = [ 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1 ]
B = 1
print(solve(A,B))





