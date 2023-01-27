def solve(A,B):

    n = len(B)
    p = 26
    pow = 1
    hash = 0
    for i in range(n-1,-1,-1):
        hash += ord(B[i]) * pow
        pow *= p


    rolling_hash =0
    pow = 1
    for i in range(n-1,-1,-1):
        rolling_hash += ord(A[i]) * pow
        pow *= p

    pow //= p

    start = 0
    end = n
    count =0

    if hash == rolling_hash:
        count += 1
    while end < len(A):
        rolling_hash = (((rolling_hash - ord(A[start]) * pow) * p) + ord(A[end]))
        start += 1
        end += 1
        if hash == rolling_hash:
            count += 1
    return count

A = "acbac"
B = "ac"
A = "aaaa"
B = "aa"
print(solve(A,B))