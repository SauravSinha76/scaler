def solve(A):
    if not A:
        return 0
        # Initialize buy1 and buy2 to negative A[0] as we want to find the maximum value.
    buy1 = buy2 = -A[0]
    # Initialize sell1 and sell2 to 0.
    sell1 = sell2 = 0

    for i in range(1, len(A)):
        # update buy1, sell1
        buy1 = max(buy1, -A[i])
        sell1 = max(sell1, buy1 + A[i])
        # update buy2, sell2
        buy2 = max(buy2, sell1 - A[i])
        sell2 = max(sell2, buy2 + A[i])
    # Return sell2 as it represents the maximum profit we can earn after two transactions.
    return sell2


A = [7, 2, 4, 8, 7]
A = [1,2,1,2]
print(solve(A))