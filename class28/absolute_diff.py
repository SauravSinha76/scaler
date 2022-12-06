def solve3(A,B,C,D):
    max_val = [- (1 << 31)] * 16
    min_val = [(1 << 31) -1] * 16


    for i in range(len(A)):
        max_val[0] = max(max_val[0], i-A[i]-B[i]-C[i]-D[i])
        min_val[0] = min(min_val[0], i-A[i]-B[i]-C[i]-D[i])

        max_val[1] = max(max_val[1], i-A[i]-B[i]-C[i]+D[i])
        min_val[1] = min(min_val[1], i-A[i]-B[i]-C[i]+D[i])

        max_val[2] = max(max_val[2], i-A[i]-B[i]+C[i]-D[i])
        min_val[2] = min(min_val[2], i-A[i]-B[i]+C[i]-D[i])

        max_val[3] = max(max_val[3], i-A[i]-B[i]+C[i]+D[i])
        min_val[3] = min(min_val[3], i-A[i]-B[i]+C[i]+D[i])

        max_val[4] = max(max_val[4], i-A[i]+B[i]-C[i]-D[i])
        min_val[4] = min(min_val[4], i-A[i]+B[i]-C[i]-D[i])

        max_val[5] = max(max_val[5], i - A[i] + B[i] - C[i] + D[i])
        min_val[5] = min(min_val[5], i - A[i] + B[i] - C[i] + D[i])

        max_val[6] = max(max_val[6], i - A[i] + B[i] + C[i] - D[i])
        min_val[6] = min(min_val[6], i - A[i] + B[i] + C[i] - D[i])

        max_val[7] = max(max_val[7], i - A[i] + B[i] + C[i] + D[i])
        min_val[7] = min(min_val[7], i - A[i] + B[i] + C[i] + D[i])

        max_val[8] = max(max_val[8], i + A[i] - B[i] - C[i] - D[i])
        min_val[8] = min(min_val[8], i + A[i] - B[i] - C[i] - D[i])

        max_val[9] = max(max_val[9], i + A[i] - B[i] - C[i] + D[i])
        min_val[9] = min(min_val[9], i + A[i] - B[i] - C[i] + D[i])

        max_val[10] = max(max_val[10], i + A[i] - B[i] + C[i] - D[i])
        min_val[10] = min(min_val[10], i + A[i] - B[i] + C[i] - D[i])

        max_val[11] = max(max_val[11], i + A[i] - B[i] + C[i] + D[i])
        min_val[11] = min(min_val[11], i + A[i] - B[i] + C[i] + D[i])

        max_val[12] = max(max_val[12], i + A[i] + B[i] - C[i] - D[i])
        min_val[12] = min(min_val[12], i + A[i] + B[i] - C[i] - D[i])

        max_val[13] = max(max_val[13], i + A[i] + B[i] - C[i] + D[i])
        min_val[13] = min(min_val[13], i + A[i] + B[i] - C[i] + D[i])

        max_val[14] = max(max_val[14], i + A[i] + B[i] + C[i] - D[i])
        min_val[14] = min(min_val[14], i + A[i] + B[i] + C[i] - D[i])

        max_val[15] = max(max_val[15], i + A[i] + B[i] + C[i] + D[i])
        min_val[15] = min(min_val[15], i + A[i] + B[i] + C[i] + D[i])

    a = - (1 << 31)
    for i in range(len(min_val)):
        if a < max_val[i] - min_val[i]:
            a = max_val[i] - min_val[i]
    print(a)

    # max1 = - 1 << 32
    # min1 = 1 << 31
    # max2 = - 1 << 32
    # min2 = 1 << 31
    #
    # for i in range(len(B)):
    #     max1 = max(max1, B[i] + i)
    #     min1 = min(min1, B[i] + i)
    #     max2 = max(max2, B[i] - i)
    #     min2 = min(min2, B[i] - i)
    #
    # print(max(max1 - min1, max2 - min2))
    #
    # max1 = - 1 << 32
    # min1 = 1 << 31
    # max2 = - 1 << 32
    # min2 = 1 << 31
    #
    # for i in range(len(C)):
    #     max1 = max(max1, C[i] + i)
    #     min1 = min(min1, C[i] + i)
    #     max2 = max(max2, C[i] - i)
    #     min2 = min(min2, C[i] - i)
    #
    # print(max(max1 - min1, max2 - min2))
    #
    # max1 = - 1 << 32
    # min1 = 1 << 31
    # max2 = - 1 << 32
    # min2 = 1 << 31
    #
    # for i in range(len(D)):
    #     max1 = max(max1, D[i] + i)
    #     min1 = min(min1, D[i] + i)
    #     max2 = max(max2, D[i] - i)
    #     min2 = min(min2, D[i] - i)
    #
    # print(max(max1 - min1, max2 - min2))

def absolute_diff(Ai,Aj,i,j):
    return abs(Ai - Aj) + abs(i -j)

def solve(A,B,C,D):
    n = len(A)
    max_diff = -( 1<< 31)
    for i in range(n):
        for j in range(i+1,n):
            diff = abs(A[i]-A[j]) + abs(B[i]-B[j]) + abs(C[i]-C[j]) + abs(D[i] -D[j]) + abs(i - j)
            max_diff = max(max_diff,diff)
    return max_diff


A = [1, 2, 3, 4]
B = [-1, 4, 5, 6]
C = [-10, 5, 3, -8]
D = [-1, -9, -6, -10]

print(solve(A,B,C,D))
print(solve3(A,B,C,D))