def solve(A, B):
    hm = {}
    ans = []
    for i in range(B):
        if A[i] in hm:
            hm[A[i]] += 1
        else:
            hm[A[i]] = 1

    ans.append(len(hm))

    start = 1
    end = B
    while end < len(A):
        hm[A[start - 1]] -= 1
        if hm[A[start - 1]] == 0:
            hm.pop(A[start - 1])

        if A[end] in hm:
            hm[A[end]] += 1
        else:
            hm[A[end]] = 1

        ans.append(len(hm))
        start += 1
        end += 1
    return ans
A = [1, 2, 1, 3, 4, 3]
B = 3
A = [1, 1, 2, 2]
B = 1
print(solve(A,B))
