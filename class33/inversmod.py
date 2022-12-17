

def pow(A,B,C):
    if A == 0:
        return 0
    if B == 0:
        return 1

    p = pow(A,B//2,C)
    x = (p * p) % C
    if B % 2 == 0:
        return x
    else:
        return (x * A) % C

def solve(A,B):

    return pow(A,B-2,B)
A = 3
B = 5

# A = 6
# B = 23
print(solve(A,B))