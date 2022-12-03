def solve(A,B):
    d ={}
    for i in range(len(A)):
        if A[i] not in d:
            d[A[i]] = 1
        else:
            d[A[i]] += 1

    ans =[]
    for i in range(len(B)):
        if B[i] not in d:
            ans.append(0)
        else:
            ans.append(d[B[i]])
    return ans

# A = [1, 2, 1, 1]
# B = [1, 2]

A = [2, 5, 9, 2, 8]
B = [3, 2]

print(solve(A,B))