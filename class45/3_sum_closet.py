def solve(A,B):
    A.sort()
    n = len(A)
    ans = 0
    min_sum = (1 << 31) -1
    for i in range(n - 2):
        l = i + 1
        r = n - 1
        while l < r:
            p = A[i] + A[l] + A[r]
            diff = abs(p - B)
            if diff < min_sum:
                min_sum = diff
                ans = p
            if p > B:
                r -= 1
            else:
                l += 1
    return ans

A = [-1, 2, 1, -4]
B = 1
A = [1, 2, 3]
B = 6
print(solve(A,B))