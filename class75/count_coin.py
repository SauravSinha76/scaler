def count(coins, n, sum):
    # If sum is 0 then there is 1
    # solution (do not include any coin)
    if (sum == 0):
        return 1

    # If sum is less than 0 then no
    # solution exists
    if (sum < 0):
        return 0

    # If there are no coins and sum
    # is greater than 0, then no
    # solution exist
    if (n <= 0):
        return 0

    # count is sum of solutions (i)
    # including coins[n-1] (ii) excluding coins[n-1]
    return count(coins, n - 1, sum) + count(coins, n, sum - coins[n - 1])

def solve_memo(coins, sum):

    dp = [[0 for _ in range(sum+1)]
          for _ in range(len(coins) + 1)]

    for i in range(len(coins) + 1):
        dp[i][0] = 1

    for i in range(1 ,len(coins) + 1):
        for j in range(1, sum + 1):
            if j - coins[i-1] >=0:
                dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[len(coins)][sum]


def solve_memo_1(coins, sum):

    dp = [0 for _ in range(sum+1)]

    dp[0] = 1

    for i in range(1 ,len(coins) + 1):
        for j in range(coins[i-1], sum + 1):
            dp[j] += dp[j- coins[i-1]]

    return dp[sum]
A = [1, 2, 3]
B = 4
print(count(A,len(A),B))
print(solve_memo(A,B))
print(solve_memo_1(A,B))