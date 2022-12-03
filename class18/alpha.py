def solve(A):
    n = len(A)
    for i in range(n):
        if not ('a' <= A[i] <= 'z') and not ('A' <= A[i] <= 'Z') and not ('0' <= A[i] <= '9'):
            return 0
    return 1

A = ['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y', '2', '0', '2', '0']
A = ['S', 'c', 'a', 'l', 'e', 'r', '#', '2', '0', '2', '0']
print(solve(A))