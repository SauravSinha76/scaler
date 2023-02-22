def solve(A):
    ans =0
    n = len(A)
    for i in range(n):
        if A[i] == '1':
            ans += 1
    return (ans * (ans +1)) // 2

A= "111"
print(solve(A))