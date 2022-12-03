def solve(A,B,C):
    max_sum =0
    for i in range(A):
        sum =0
        for j in range(i,A):
            sum += C[j]
            if max_sum < sum <= B:
                max_sum = sum

    return max_sum


A = 5
B = 12
C = [2, 1, 3, 4, 5]
# A = 3
# B = 1
# C = [2, 2, 2]
print(solve(A,B,C))