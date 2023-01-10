def solve(A):
    n = len(A)

    max_val = max(A)
    min_val = min(A)

    range_val = max_val - min_val +1
    freq = [0 for i in range(range_val)]

    for i in range(n):
        idx = A[i] - min_val
        freq[idx] += 1


    for i in range(1,range_val):
        freq[i] += freq[i-1]

    ans =[0 for i in range(n)]
    for i in range(n-1,-1,-1):
        idx = freq[A[i] - min_val] - 1
        ans[idx] = A[i]
        freq[A[i]-min_val] -= 1
    return ans

A = [1, 3, 1]
A = [4, 2, 1, 3]
print(solve(A))