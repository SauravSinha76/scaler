def solve(A):
    n = len(A)

    hm ={}

    hm[0] = [-1]

    res =0
    xor = 0
    for i in range(n):
        xor ^= A[i]

        if xor in hm:
            for idx in hm[xor]:
                res += i - idx -1
            hm[xor].append(i)
        else:
            hm[xor] = [i]

    return res % (10**9 + 1)

A = [5, 2, 7]
print(solve(A))