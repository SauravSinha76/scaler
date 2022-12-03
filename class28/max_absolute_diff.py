def solve(A):

    max1 = - 1 << 32
    min1 = 1 << 31
    max2 = - 1 << 32
    min2 = 1 << 31

    for i in range(len(A)):
        max1 = max(max1, A[i] + i)
        min1 = min(min1, A[i] + i)
        max2 = max(max2, A[i] - i)
        min2 = min(min2, A[i] - i)

    return max(max1 - min1, max2 - min2)



A = [1, 3, -1]
print(solve(A))
