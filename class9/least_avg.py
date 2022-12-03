def solve(A,B):

    n = len(A)

    sum =0
    for i in range(B):
        sum += A[i]

    min_sum = sum
    min_i = 0

    start = 1
    end =B

    while end < n:
        sum += A[end] - A[start-1]

        if sum < min_sum:
            min_sum = sum
            min_i = start

        start += 1
        end += 1

    return min_i

# A=[3, 7, 90, 20, 10, 50, 40]
# B=3
A=[3, 7, 5, 20, -10, 0, 12]
B=2

print(solve(A,B))