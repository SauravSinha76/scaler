def solve(A):
    X =0
    pos =0
    for i in range(31,-1,-1):
        if A & 1 << i:
            pos = i+1
            break
    for i in range(pos):
        if not (A & 1 << i):
            X += 1 << i
    Y = 1 << pos
    return X ^ Y

A = 5
print(solve(A))
