def solve(A,i,B,C,cost):
    if i == 0:
        return cost
    if i > 1:
        return min(solve(A,i-1,B,C,cost + B * abs(A[i] - A[i-1])),solve(A,i-2,B,C,cost + C *abs(A[i] - A[i-2])))
    else:
        return solve(A,i-1,B,C,cost + B *(A[i] - A[i-1]))

def solve_memo(A,B,C,i,cost,dp):
    if i == 0:
        return cost
    if dp[i] != -1:
        return dp[i]
    if i > 1:
        dp[i] = min(solve_memo(A,B,C,i-1,cost + B * abs(A[i] - A[i-1]),dp),solve_memo(A,B,C,i-2,cost + C *abs(A[i] - A[i-2]),dp))
    else:
        dp[i] = solve_memo(A,B,C,i-1,cost + B *abs(A[i] - A[i-1]),dp)
    return dp[i]
def solve_tab(A,B,C):
    n = len(A)
    dp = [0] * n

    dp[1] = B *abs(A[1] - A[0])

    for i in range(2,n):
        dp[i] = min( dp[i-1] + B * abs(A[i] - A[i-1]), dp[i-2] + C * abs(A[i] - A[i-2]))

    return dp[n-1]
A =[1,2,3]
B = 2
C = 3
# A =[10,100]
# B = 20
# C = 30
A = [63,65,6,46,82]
# A = [63,65,6,46,82]
B = 79
C = 59
print(solve(A,len(A)-1,B,C,0))
dp =[-1] * len(A)
print(solve_memo(A,B,C,len(A)-1,0,dp))
print(solve_tab(A,B,C))