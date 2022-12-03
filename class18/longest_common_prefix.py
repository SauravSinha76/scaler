import sys


def solve(A):
    n = len(A)
    max_prefix_len = sys.maxsize
    for i in range(n-1):
        j =0
        p = min(len(A[i]),len(A[i+1]))
        q = min(max_prefix_len,p)
        while j < q and A[i][j] == A[i+1][j]:
            j += 1

        max_prefix_len = j

    return A[n-1][0:max_prefix_len]

A = ["abcdefgh", "aefghijk", "abcefgh"]
A = ["abab", "ab", "abcd"]
print(solve(A))

