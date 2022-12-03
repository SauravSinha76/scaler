def solve(A):
    n = len(A)

    for i in range(n):
        if 'a' <= A[i] <= 'z':
            A[i] = chr(ord(A[i]) ^ (1 << 5))
    return A

A = ['S', 'c', 'A', 'L', 'E', 'r', 'A', 'c', 'a', 'D', 'e', 'm', 'y']
print(solve(A))