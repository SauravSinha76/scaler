def solve(A,B):
    A.sort()
    B.sort()
    n = len(A)
    min_time = 0

    for i in range(n):
        diff = abs(A[i] - B[i])

        min_time = max(min_time,diff)
    return min_time

A = [-4, 2, 3]
B = [0, -2, 4]
A = [-2]
B = [-6]
print(solve(A,B))