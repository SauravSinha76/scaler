def solve(A):
    hm = {}
    n = len(A)
    start = 0
    max_length = 0
    for i in range(n):
        if A[i] in hm:
            start = max(start, hm[A[i]] + 1)

        max_length = max(max_length, i - start + 1)

        hm[A[i]] = i
    return max_length

A = "abcabcbb"
print(solve(A))