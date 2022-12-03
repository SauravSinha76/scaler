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


A = 2
B = 3
C = 3

A = 0
B = 0
C = 3

print(pow(A,B,C))