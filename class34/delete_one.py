def gcd(a,b):
    if b == 0:
        return a
    return gcd(b , a % b)

def array_gcd(A):
    n = len(A)
    ans = A[0]
    for i in range(1,n):
        if ans != 1:
            ans = gcd(ans,A[i])
    return ans

def solve(A):
    n = len(A)
    max_gcd = 0
    for i in range(n-1):
        if i == 0:
            gcd_array = array_gcd(A[1:n])
        else:
            gcd_array = gcd(array_gcd(A[0:i]),array_gcd(A[i+1:n]))
        max_gcd = max(max_gcd,gcd_array)
    return max_gcd


def solve1(A):
    n = len(A)
    prefix_gcd = [0] * n
    suffix_gcd = [0] * n

    prefix_gcd[0] = A[0]
    for i in range(1,n):
        prefix_gcd[i] = gcd(prefix_gcd[i-1],A[i])
    suffix_gcd[n-1] = A[n-1]
    for i in range(n-2,-1,-1):
        suffix_gcd[i] = gcd(A[i],suffix_gcd[i+1])

    print(suffix_gcd)
    print(prefix_gcd)
    max_gcd = 0
    for i in range(n):
        if i ==0:
            gcd_val = suffix_gcd[1]
        elif i == n-1:
            gcd_val = prefix_gcd[n-2]
        else:
            gcd_val = gcd(prefix_gcd[i-1],suffix_gcd[i+1])
        max_gcd = max(max_gcd,gcd_val)
    return max_gcd

A = [12, 15, 18]
print(solve(A))
print(solve1(A))
