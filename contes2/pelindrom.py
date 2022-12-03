def solve(A):
    n = len(A)
    hm = [0] * 26
    for s in A:
        hm[ord(s) - ord('a')] += 1

    odd_count = 0
    for a in hm:
        if a % 2 == 1:
            odd_count += 1
    if odd_count < 2:
        return 1
    else:
        return 0

A = "aabb"
print(solve(A))