def solve(A):
    dp =[0]
    for i in range(1,len(A)+1):
        dp.append(A[i-1])

    for i in range(2, len(A)+1):
        left = 0
        right = i
        while left <= right:
            dp[i] = max(dp[i], dp[left] + dp[right])
            left += 1
            right -= 1
    return dp[len(A)]

A = [3, 4, 1, 6, 2]
A = [1, 5, 2, 5, 6]
print(solve(A))