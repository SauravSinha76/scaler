def solve(A,B):

    n = len(A)

    i =0
    j = n-1
    count =0
    while i <= j:
        area = A[i] * A[j]
        if area >= B:
            j -= 1
        else:
            count += 2 *(j - i) + 1
            i += 1
    return count

A = [1, 2]
B = 1
# A = [ 1, 2, 3, 4, 5 ]
# B = 5

print(solve(A,B))

