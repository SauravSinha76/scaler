def solve(A,B):
    if len(A) == B:
        return 1
    count = [0] * 26
    ans = 0
    for i in range(len(A)):
        count[ord(A[i]) - ord('a')] += 1
        if count[ord(A[i]) - ord('a')] == 1:
            ans += 1

    count.sort()
    for i in range(len(count)):
        if count[i] != 0 and B - count[i] >= 0:
            B -= count[i]
            ans -= 1

    return ans

A = "abcabbccd"
B = 3
print(solve(A,B))
