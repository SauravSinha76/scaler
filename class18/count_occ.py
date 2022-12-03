def solve(A):
    n = len(A)
    B = "bob"
    b = len(B)
    ans = 0
    for i in range(n):
        if A[i:i + b] == B:
            ans += 1

    return ans


A = "abobc"
A = "bobob"
print(solve(A))
