import sys


def solve(A):
    max_sum = - 1 << 32
    sum = 0
    for i in range(len(A)):
        sum += A[i]
        if sum < 0:
            sum = 0
        max_sum = max(max_sum,sum)
    return max_sum

# A = [1, 2, 3, 4, -10]
A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(solve(A))
