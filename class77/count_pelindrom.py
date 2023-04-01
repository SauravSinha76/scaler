def solve(A):
    n = len(A)
    dp =[[False] * n for _ in range(n)]
    for gap in range(n):
        i = 0
        j = gap
        while j < n:
            if gap == 0:
                dp[i][j] = True
            elif gap == 1:
                dp[i][j] = A[i] == A[j]
            else:
                if A[i] != A[j]:
                    dp[i][j] = False
                else:
                    dp[i][j] = dp[i+1][j-1]
            i +=1
            j += 1
    count =0
    for i in range(n):
        for j in range(i,n):
            if dp[i][j]:
                count += 1
    return count

A = "abab"
A = "ababa"
A = "bbeaadcc"
print(solve(A))