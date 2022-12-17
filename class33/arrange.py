def solve(A):
    n = len(A)

    for i in range(n):
        A[i] *= n

    for i in range(n):
        idx = A[i] // n
        val = A[idx] // n
        A[i] += val

    for i in range(n):
        A[i] %= n
    return A

A =[1,2,3,4,0]
print(solve(A))