def solve(A):
    n = len(A)

    for i in range(n):
        for j in range(i+1,n):
            A[i][j],A[j][i] = A[j][i],A[i][j]

    for i in range(n):
        left =0
        right = n-1
        while left< right:
            A[i][left], A[i][right] = A[i][right], A[i][left]
            left += 1
            right -= 1

A= [
    [1, 2],
    [3, 4]
 ]
solve(A)
print(A)
