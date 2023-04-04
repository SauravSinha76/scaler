def solve(A):
    n = len(A)

    profit =0
    for i in range(1,n):
        if A[i] > A[i-1]:
            profit += A[i] - A[i-1]
    return profit

A = [1, 2, 3]
A = [5, 2, 10]
print(solve(A))