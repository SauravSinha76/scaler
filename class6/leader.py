def solve(A):
    n = len(A)
    leader = [A[n - 1]]
    max_val = A[n-1]
    for i in range(n-2,-1,-1):
        if max_val < A[i]:
            max_val = A[i]
            leader.append(A[i])
    return leader

A = [16, 17, 4, 3, 5, 2]
print(solve(A))