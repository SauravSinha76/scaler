def solve(A,B):
    hm ={}
    count =0
    for i in range(len(A)):
        b1 = A[i] - B
        b2 = A[i] + B

        if b1 in hm:
            count += hm[b1]
        if b2 in hm:
            count += hm[b2]

        if A[i] in hm:
            hm[A[i]] += 1
        else:
            hm[A[i]] = 1

    return count % (10 ** 9+7)

A = [3, 5, 1, 2]
B = 4
A = [1, 2, 1, 2]
B = 1
print(solve(A,B))