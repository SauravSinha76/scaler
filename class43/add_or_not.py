def solve(A,B):
    A.sort()
    n = len(A)
    ans= [-1,-1]
    psum =[0,A[0]]
    for i in range(1,n):
        psum.append(psum[i]+A[i])
    for i in range(n):
        count = 0
        ops = B
        for j in range(i,-1,-1):
            if A[i] * (i - j +1) - (psum[i+1] - psum[j]) <= ops:
                count = i - j +1
            if count > ans[0]:
                ans[0] = count
                ans[1] = A[i]
    return ans

def solve2(A,B):
    A.sort()
    n = len(A)
    ans =[-1,-1]
    psum = [0,A[0]]
    for i in range(1,n):
        psum.append(psum[i] + A[i])
    count =0
    for i in range(n):
        low = 0
        high = i
        while low <= high:
            mid = (low + high) // 2
            if A[i] * (i - mid + 1) - (psum[i + 1] - psum[mid]) <= B:
                count = (i - mid + 1)
                high = mid -1
            else:
                low = mid + 1

        if count > ans[0]:
            ans[0] = count
            ans[1] = A[i]
    return ans

A = [3,1,2,2,1]
B = 3
print(solve(A,B))
print(solve2(A,B))