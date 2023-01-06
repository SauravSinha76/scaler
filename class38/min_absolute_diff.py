def solve(A):
    A.sort()
    ans = 1 << 31 -1
    for i in range(len(A)-1):
        ans = min(ans, A[i+1] - A[i])
    return ans
A = [1, 2, 3, 4, 5]
A = [5, 17, 100, 11]
print(solve(A))