def solve(A):
    l = 0
    r = A
    ans =0
    while l <= r:
        mid = (l + r) // 2
        if mid * mid > A:
            r = mid - 1
        else:
            ans = mid
            l = mid + 1
    return ans
A = 11
print(solve(A))