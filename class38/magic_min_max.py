def solve(A):
    n = len(A)

    A.sort()

    max_val =0
    min_val =0
    i =0
    j =0
    while i < n//2:
        max_val += A[n-i-1] - A[i]
        i+= 1

    while j < n:
        min_val += A[j+1] - A[j]
        j += 2

    return [max_val,min_val]

A = [3, 11, -1, 5]
A = [2, 2]
print(solve(A))