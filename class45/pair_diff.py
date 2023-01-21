def solve(A,B):
    A.sort()
    B = abs(B)
    n = len(A)

    i = 0
    j = 1
    count =0

    while j < n:
        diff = A[j] - A[i]

        if diff == B:
            count += 1
            j += 1
            while j < n and A[j-1] == A[j]:
                j += 1
            i += 1
            while i < j and A[i-1] == A[i]:
                i += 1
        elif diff < B:
            j += 1
        else:
            i += 1
            if i == j:
                j += 1
    return count

A = [8, 12, 16, 4, 0, 20]
B = 4
A = [ 8, 5, 1, 10, 5, 9, 9, 3, 5, 6, 6, 2, 8, 2, 2, 6, 3, 8, 7, 2, 5, 3, 4, 3, 3, 2, 7, 9, 6, 8, 7, 2, 9, 10, 3, 8, 10, 6, 5, 4, 2, 3 ]
B = 3
# A = [1, 5, 3, 4, 2]
# B = 3
# A = [1, 1, 1, 1, 1]
# B = 0
A = [ 1, 2 ]
B = 0
print(solve(A,B))