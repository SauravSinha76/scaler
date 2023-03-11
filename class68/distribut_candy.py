def solve(A):
    n = len(A)

    candies = [1] * n

    for i in range(1,n):
        if A[i] > A[i-1]:
            candies[i] = candies[i-1] + 1

    for i in range(n-2,-1,-1):
        if A[i] > A[i+1] and candies[i] <= candies[i+1]:
            candies[i] = candies[i+1] + 1

    return sum(candies)

A = [1, 2]
A = [1, 5, 2, 1]
print(solve(A))
