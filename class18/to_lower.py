def solve(A):
    n = len(A)
    for i in range(n):
        if 'A' <= A[i] <= 'Z':
            A[i] = chr(ord(A[i])^(1 << 5))
    return A

A = ['S', 'c', 'A', 'l', 'e', 'r', 'A', 'c', 'a', 'D', 'e', 'm', 'y']
A = ['S', 'c', 'a', 'L', 'e', 'r', '#', '2', '0', '2', '0']
print(solve(A))