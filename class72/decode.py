def solve(A):
    if len(A) == 2:
        if A < "27":
            return 2
        else:
            return 0
    if len(A) == 1:
        return len(A)

    return (solve(A[1:]) + solve(A[2:])) % (10 ** 9 + 7)

def solve_memo(A,dp):
    if len(A) == 2:
        if A < "27":
            return 2
        else:
            return 0
    if len(A) == 1:
        return len(A)

    if dp[len(A)] != -1:
        return dp[len(A)]

    dp[len(A)] = (solve_memo(A[1:],dp) + solve_memo(A[2:],dp)) % (10 ** 9 + 7)
    return dp[len(A)]

def solve_tab(A):

    dp = [0 for _ in range(len(A)+1)]

    if A[0] == '0':
        return 0
    dp[0] = 1
    dp[1] = 1

    for i in range(2,len(A)+1):
        if A[i-1] != '0':
            dp[i] = dp[i-1]
        if A[i-2] == '1' or (A[i-2] == '2' and A[i-1] <= '6'):
            dp[i] = (dp[i] + dp[i-2]) % (10 ** 9 + 7)

    return dp[len(A)]
A = "516349039"
print(solve(A))
dp = [-1 for _ in range(len(A)+1)]
print(solve_memo(A,dp))
print(solve_tab(A))

