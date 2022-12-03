import sys


def solve(A,B):
    n = len(B)
    ans = sys.maxsize
    for i in range(n - 2):
        if B[i] < ans:
            for j in range(i + 1, n - 1):
                if B[i] + B[j] < ans and A[i] < A[j]:
                    for k in range(j + 1, n):
                        if A[j] < A[k] and (B[i] + B[j] + B[k]) < ans:
                            ans = B[i] + B[j] + B[k]

    if ans == sys.maxsize:
        return -1
    else:
        return ans

# A = [1, 3, 5]
# B = [1, 2, 3]
A = [1, 6, 4, 2, 6, 9]
B = [2, 5, 7, 3, 2, 7]
print(solve(A,B))