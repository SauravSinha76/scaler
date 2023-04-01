def checkPelindrom(A,start,end):
    while start < end:
        if A[start] != A[end]:
            return False
        start += 1
        end -= 1
    return True

def mincut(A,start,end,dp):
    if checkPelindrom(A,start,end):
        return 0

    if dp[start][end] != -1:
        return dp[start][end]

    min_cut = 1 << 31 -1
    for i in range(start,end):
        if checkPelindrom(A,start,i):
            min_cut = min(min_cut,mincut(A,i+1,end,dp))

    dp[start][end] = min_cut + 1

    return dp[start][end]

def solve(A):
    n = len(A)
    dp= [[-1] * n for _ in range(n)]
    return mincut(A,0,n-1,dp)

A = "aab"
print(solve(A))