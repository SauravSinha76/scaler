def solve(A):
    n = len(A)
    s = ""
    for i in range(n):
        s += chr(ord(A[i]) ^ (1 << 5))
    return s

A = "Hello"
print(solve(A))