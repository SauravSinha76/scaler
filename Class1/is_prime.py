from math import sqrt


def solve(A):
    if A == 1:
        return 0
    i =2
    while i*i <= A:
        if A % i == 0:
            return 0
        i += 1
    return 1
print(solve(17))