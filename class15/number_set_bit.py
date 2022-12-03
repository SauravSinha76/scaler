def solve(A):
    count =0
    while A >0:
        if A & 1:
            count += 1
        A = A >> 1
    return count

A = 11
print(solve(A))