def solve(A):
    n = len(A)
    sum =0
    i = 0
    j = n-1
    while( i< n and j > -1):
        sum += A[i][j]
        i += 1
        j -= 1
    return sum

# A = [[1, -2, -3],
#       [-4, 5, -6],
#       [-7, -8, 9]]
A = [[3, 2],
      [2, 3]]
print(solve(A))