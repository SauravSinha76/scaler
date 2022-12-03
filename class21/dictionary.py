def solve(A, B):
    hm = {}
    for i in range(len(B)):
        hm[B[i]] = i

    for i in range(len(A) - 1):
        str_len = min(len(A[i]), len(A[i + 1]))
        j = 0
        while j < str_len:
            if hm[A[i][j]] > hm[A[i + 1][j]]:
                return 0
            elif hm[A[i][j]] == hm[A[i + 1][j]]:
                j += 1
            else:
                break
        if len(A[i]) > len(A[i + 1]):
            return 0
    return 1


A = ["hello", "scaler", "interviewbit"]
B = "adhbcfegskjlponmirqtxwuvzy"
A = ["fine", "none", "no"]
B = "qwertyuiopasdfghjklzxcvbnm"
print(solve(A, B))
