def solve(A,B,C):
    n = len(A)
    sum =0
    for i in range(B):
        sum += A[i]

    if sum == C:
        return 1
    start =1
    end = B
    while end < n:
        sum += A[end] - A[start-1]
        start += 1
        end += 1
        if sum == C:
            return 1
    return 0

A = [4, 3, 2, 6]
B = 2
C = 5

# A = [4, 2, 2]
# B = 2
# C = 8

# A = [ 6 ]
# B = 1
# C = 6
print(solve(A,B,C))
