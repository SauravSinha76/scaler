def solve(A,B):
    ans =[0] * A
    n = len(B)
    for i in range(n):
        s = B[i][0]-1
        e = B[i][1]
        val = B[i][2]

        ans[s] += val
        if e < A:
            ans[e] += - val

    for i in range(1,A):
        ans[i] += ans[i-1]
    return ans

A = 5
B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
print(solve(A,B))