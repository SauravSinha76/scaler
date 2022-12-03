def solve(A,B):
    n = len(A)
    sum =0
    for i in range(B):
        sum += A[i]

    max_sum = sum
    for i in range(B):
        sum += (A[n-i-1] -A[B-i-1])
        if max_sum < sum:
            max_sum = sum
    return max_sum
# A = [5, -2, 3 , 1, 2]
# B = 3
A = [1, 2]
B = 1
print(solve(A,B))