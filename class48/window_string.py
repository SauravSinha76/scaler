def solve(A,B):
    hm_b = {}
    n, k = len(A), len(B)

    for i in range(k):
        hm_b[B[i]] = hm_b.get(B[i], 0) + 1
    l, r = 0, 0
    count = k
    min_len = n
    start, end = 0, n - 1

    found = False
    while r < n:
        if A[r] in hm_b:
            hm_b[A[r]] -= 1
            if hm_b[A[r]] >= 0:
                count -= 1
        r += 1

        if count > 0:
            continue

        while count == 0:
            if A[l] in hm_b:
                hm_b[A[l]] += 1
                if hm_b[A[l]] > 0:
                    count += 1
            l += 1

        if (r - l) < min_len:
            found = True
            start = l
            end = r
            min_len = r - l

    if found:
        if start == 0:
            return A[start:end]
        return A[start - 1:end]

    return ""

A = "ADOBECODEBANC"
B = "ABC"
print(solve(A,B))