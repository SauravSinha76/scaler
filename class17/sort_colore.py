def solve(A):
    zero = 0
    one = 0
    two = 0
    n = len(A)
    for i in range(n):
        if A[i] ==0:
            zero += 1
        elif A[i] == 1:
            one += 1
        elif A[i] == 2:
            two += 1

    pos =0
    j =0
    while j < zero:
        A[pos] = 0
        j += 1
        pos += 1
    j =0
    while j < one:
        A[pos] = 1
        j += 1
        pos += 1
    j = 0
    while j < two:
        A[pos] = 2
        j += 1
        pos += 1

    return A

A = [0, 1, 2, 0, 1, 2]
print(solve(A))