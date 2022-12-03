def solve(A):
    n = len(A)
    max_val = A[0]
    min_val = A[0]

    for i in range(1, n):
        if max_val < A[i]:
            max_val = A[i]

    for i in range(1, n):
        if min_val > A[i]:
            min_val = A[i]

    if max_val == min_val: return 1

    max_idx = -1
    min_idx = -1
    ans = n

    for i in range(n):
        if A[i] == min_val:
            min_idx = i
            if max_idx != -1:
                ans = min(ans, min_idx - max_idx + 1)
        elif A[i] == max_val:
            max_idx = i
            if min_idx != -1:
                ans = min(ans, max_idx - min_idx + 1)
    return ans


A = [2]
print(solve(A))
