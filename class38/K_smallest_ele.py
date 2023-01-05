def solve(A,B):
    A = list(A)
    n = len(A)

    for i in range(B):
        min_val = A[i]
        min_idx = i
        for j in range(i+1, n):
            if min_val > A[j]:
                min_val = A[j]
                min_idx = j

        if min_idx != i:
            tmp = A[i]
            A[i] = A[min_idx]
            A[min_idx] = tmp

    return A[B-1]


A = (2, 1, 4, 3, 2)
B = 3
print(solve(A,B))