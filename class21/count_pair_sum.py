def solve(A,B):
    hm = {}
    count = 0
    for i in range(len(A)):
        b = B - A[i]

        if b in hm:
            count += hm[b]

        if A[i] in hm:
            hm[A[i]] += 1
        else:
            hm[A[i]] = 1

    return count

A = [3, 5, 1, 2]
B = 8
A = [1, 1, 1, 1]
B = 2
print(solve(A,B))

