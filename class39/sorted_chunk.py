def solve(A):
    n = len(A)
    max_val = - 1
    count =0
    for i in range(n):
        max_val = max(max_val,A[i])
        if max_val == i:
            count += 1
    return count

A = [1, 2, 3, 4, 0]
A = [2, 0, 1, 3]
print(solve(A))
