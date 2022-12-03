def solve(A,B):
    n = len(A)
    count =0
    for i in range(n):
        sum =0
        for j in range(i,n):
            sum += A[j]
            if sum < B:
                count += 1
    return count

# A = [2, 5, 6]
# B = 10
A = [1, 11, 2, 3, 15]
B = 10
print(solve(A,B))