def solve(A,B):
    hm = {}
    count =0
    for i in range(len(A)):
        b = B ^ A[i]

        if b in hm:
            count += hm[b]

        if A[i] in hm:
            hm[A[i]] += 1
        else:
            hm[A[i]] = 1

    return count

A = [5, 4, 10, 15, 7, 6]
B = 5
A = [3, 6, 8, 10, 15, 50]
B = 5
print(solve(A,B))