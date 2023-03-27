def solve(A):
    n = len(A)
    S = set(A)
    max_l =0
    for i in range(n):
        for j in range(i+1, n):

            x = A[j]
            y = A[i] + A[j]

            l = 2

            while y in S:
                z = x + y
                x = y
                y = z
                l += 1

            max_l = max(l,max_l)
    return max_l

A = [1, 2, 3, 4, 5, 6, 7, 8]
A = [ 8, 9, 14, 17, 26, 27, 36, 38, 43, 51 ]
print(solve(A))
