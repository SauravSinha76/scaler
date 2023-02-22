def solve(A):
    hm ={}

    for a in A:
        hm[a] = hm.get(a,0) + 1

    return len(hm)

A ="abacbc"
A="abdca"
print(solve(A))