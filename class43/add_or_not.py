def solve(A,B):
    A.sort()
    n = len(A)
    ans= [-1,-1]

    for i in range(n):
        count = 0
        ops = B
        for j in range(i,-1,-1):
            if A[i] - A[j] <= ops:
                count += 1
                ops -= (A[i] - A[j])
            if count > ans[0]:
                ans[0] = count
                ans[1] = A[i]
    return ans

A = [3,1,2,2,1]
B = 3
print(solve(A,B))