def tab_solve(A, B,used):
    n = len(A)
    m = len(B)

    dp = [[0 for _ in range(m + 1)]
          for _ in range(n + 1)]
    # dp[0][0] = True
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if not used[j-1]:
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    used[j-1] = True
                else:
                    dp[i][j] = max(dp[i - 1][j] , dp[i][j - 1])
    return dp[n][m]

def solve(A,B,C):
    k = len(C)
    used =[False] * k
    if len(A) == tab_solve(A, C,used) and len(B) == tab_solve(B, C,used):
        return 1
    else:
        return 0


def inter_leaving_string(B, C, dp):
    k = len(B)-1
    j = len(C)-1
    while k > -1 and j > -1:
        if not dp[j] and B[k] == C[j]:
            dp[j] = True
            k -= 1
            j -= 1
        else:
            j -= 1
    return k


A = "aabcc"
B = "dbbca"
C = "aadbbcbcac"
# A = "aabcc"
# B = "dbbca"
# C = "aadbbbaccc"
# A = "LgR8D8k7t8KIprKDTQ7aoo7ed6mhKQwWlFxXpyjPkh"
# B = "Q7wQk8rqjaH971SqSQJAMgqYyETo4KmlF4ybf"
# C = "Q7wLgR8D8Qkk7t88KIrpqjarHKD971SqSQJTQ7aoAMgoq7eYd6yETmhoK4KmlQwWFlF4xybXfpyjPkh"
# print(tab_solve(A,C))
# print(tab_solve(B,C))
print(solve(A,B,C))