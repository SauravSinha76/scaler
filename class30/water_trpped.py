def solve(A):
    n = len(A)
    lmax = [0] *n
    rmax = [0] *n

    lmax[0] = A[0]
    rmax[n-1] = A[n-1]

    for i in range(1,n):
        if A[i] > lmax[i-1]:
            lmax[i] = A[i]
        else:
            lmax[i] = lmax[i-1]

    for i in range(n-2,-1,-1):
        if A[i] > rmax[i+1]:
            rmax[i] = A[i]
        else:
            rmax[i] = rmax[i+1]

    ans = 0
    for i in range(1,n-1):
        ans += min(lmax[i],rmax[i]) - A[i]

    return ans

A = [1,  2]
print(solve(A))
