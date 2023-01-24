def solve(A):
    n = len(A)

    hm ={}
    min_distance = (1 << 31) -1
    for i in range(n):
        if A[i] not in hm:
            hm[A[i]] =i
        else:
            distance = i - hm[A[i]]
            min_distance = min(min_distance,distance)
            hm[A[i]] = i
    return min_distance

A = [7, 1, 3, 4, 1, 7]
A = [1, 1]
print(solve(A))