def gcd(A,B):
    if B == 0:
        return A
    return gcd(B, A%B)

def lcm(A,B):
    return (A*B) // gcd(A,B)

def count_magic(B,C,mid):
    return mid // B + mid // C - mid // lcm(B,C)

def solve(A,B,C):

    l = min(B,C)
    r = A*min(B,C)
    ans = -1
    while l <= r:
        mid = (l+r) // 2
        pos = count_magic(B,C,mid)

        if pos >= A:
            ans = mid
            r = mid -1
        else:
            l = mid + 1
    return ans

A = 1
B = 2
C = 3

A = 4
B = 2
C = 3
print(solve(A,B,C))