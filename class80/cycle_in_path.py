import sys


def solve(A,B,C):
    if B == C:
        return 1
    i = B -1
    while i >0:
        if A[i] == C:
            return 1
        else:
            i = A[i] -1
    return 0


A = [1, 1, 2]
B = 2
C = 1
print(solve(A,B,C))