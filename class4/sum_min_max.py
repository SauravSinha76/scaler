def solve(A):
    n = len(A)
    min_A = A[0]
    max_A= A[0]
    for i in range(1,n):
        if min_A > A[i]:
            min_A = A[i]
        if max_A < A[i]:
            max_A = A[i]
    return max_A+ min_A


A = [-2, 1, -4, 5, 3]
print(solve(A))