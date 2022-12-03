import math


def solve(A):
    i =0
    while i*i <= A:
        if i*i ==A:
            return i
        i += 1
    return -1


print(solve(math.pow(10,8)))