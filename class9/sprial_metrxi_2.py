def solve(A):
    res = [[0 for column in range(A)]
           for row in range(A)]
    i = 0
    j = 0
    num = 1
    while A > 1:
        for _ in range(1,A):
            res[i][j] = num
            num += 1
            j += 1

        for _ in range(1,A):
            res[i][j] = num
            num += 1
            i += 1

        for _ in range(1,A):
            res[i][j] = num
            num += 1
            j -= 1

        for _ in range(1,A):
            res[i][j] = num
            num += 1
            i -= 1

        i += 1
        j += 1
        A -= 2

    if A == 1:
        res[i][j] = num

    return res

print(solve(5))


