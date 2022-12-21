import sys
def factorial(a,p):
    fact = 1
    for i in range(2,a+1):
        fact = (fact * i) % p
    return fact

def power(A,B,P):

    if A == 0:
        return 0
    if B == 0:
        return 1

    val = power(A, B//2, P)
    x = (val * val) % P
    if B & 1:
        return (A * x) % P
    else:
        return x

def solve(A,B,C):
    # if N == R:
    #     return 0

    num = 1
    den = 1
    for i in range(B):
        num = (num * (A - i)) % C
        den = (den * (i+1)) % C
    num_3 = 0
    if C > 1:
        num_3 = power(den,C-2,C)
    return (num * num_3) % C

def solve_dp(A,B,C):
    mat = [[0 for column in range(B+1)]
                for row in range(A+1)]

    for i in range(A+1):
        mat[i][0] = 1

    for i in range(1,A+1):
        for j in range(1, B+1):
            mat[i][j] = (mat[i-1][j-1] + mat[i-1][j]) % C
    return mat[A][B]

sys.setrecursionlimit(10**6)
print(solve(5,2,13))