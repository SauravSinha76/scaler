def solve(A):
    n = len(A)
    max_sell = 0
    max_profit = 0
    for i in range(n-1,-1,-1):
        if max_sell < A[i]:
            max_sell = A[i]

        profit = max_sell - A[i]
        if max_profit < profit:
            max_profit = profit
    return max_profit

A = [1, 4, 5, 2, 4]
print(solve(A))
