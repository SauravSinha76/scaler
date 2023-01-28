def solev(A,B):

    n = len(B)
    hm = {}

    for i in range(n):
        hm[B[i]] = hm.get(B[i],0) + 1

    for key in hm:
        if hm[key] % A != 0:
            return -1
    return 1

A = 2
B = "bbaabb"
A = 1
B = "bc"
print(solev(A,B))
