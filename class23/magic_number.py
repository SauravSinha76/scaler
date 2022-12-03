def recusiv_sum(A):
    if A == 0:
        return 0
    r = A % 10
    A = A // 10
    return recusiv_sum(A) + r

def solve(A):
    if A // 10 == 0:
        if A == 1:
            return 1
        else:
            return 0

    return solve(recusiv_sum(A))


print(solve(1291))