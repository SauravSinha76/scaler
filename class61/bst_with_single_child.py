def solve(A):
    n = len(A)
    max_so_far = min_so_far = A[-1]

    for i in range(n-2, -1, -1):
        if not (A[i] < min_so_far or A[i] > max_so_far):
            return "NO"

        max_so_far = max(A[i], max_so_far)
        min_so_far = min(A[i], min_so_far)
    return "YES"

A = [4, 10, 5, 8]
A= [1, 5, 6, 4]
print(solve(A))
