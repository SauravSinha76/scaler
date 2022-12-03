def solve(A,B):
    ans =0
    t =1
    n = len(A)
    for i in range(n-1,-1,-1):
        ans = (A[i]*t + ans) % B
        t = (t * 10) % B
    return ans

A = [1, 4, 3]
B = 2

A = [4, 3, 5, 3, 5, 3, 2, 1]
B = 47
print(solve(A,B))