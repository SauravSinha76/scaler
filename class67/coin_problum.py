def solve(A):

    p = 5

    count =0
    while A > 0:
        v = 1
        prv_v = 1
        while v <= A:
            prv_v = v
            v = v * p

        A = A - prv_v
        count += 1
    return count

print(solve(35))

