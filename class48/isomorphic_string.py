def solve(A,B):
    if len(A) != len(B):
        return 0

    n = len(A)

    count_a = [0] * 26
    count_b = [0] * 26
    for i in range(n):
        count_a[ord(A[i]) - ord('a')] += 1
        count_b[ord(B[i]) - ord('a')] += 1
    for i in range(n):
        if count_a[ord(A[i]) - ord('a')] != count_b[ord(B[i]) - ord('a')]:
            return 0
    return 1

A = "aba"
B = "zyz"
print(solve(A,B))
