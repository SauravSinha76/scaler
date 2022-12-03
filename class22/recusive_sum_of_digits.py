import sys
def recusiv_sum(A):
    if A == 0:
        return 0
    r = A % 10
    A = A // 10
    return recusiv_sum(A) + r


sys.setrecursionlimit(10 ** 6)
A = 46
print(recusiv_sum(A))