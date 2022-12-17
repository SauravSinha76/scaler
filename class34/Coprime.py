def gcd(A,B):
    if B == 0:
        return A
    return gcd(B, A%B)

def solve(A,B):
    while gcd(A,B) != 1:
        A = A // gcd(A,B)
    return A

print(solve(5,10))
