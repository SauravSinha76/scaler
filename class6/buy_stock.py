def solve(A):
    n = len(A)
    if n <2:
        return 0

    buy = A[0]
    max_profit = 0
    for i in range(1,n):
        if buy > A[i]:
            buy = A[i]
        elif max_profit < A[i] - buy:
            max_profit = A[i] - buy
    return max_profit

A = [1, 4, 5, 2, 4]
print(solve(A))