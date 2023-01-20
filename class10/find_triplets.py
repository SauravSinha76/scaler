def solve(A):
    n = len(A)
    ans =0
    for i in range(1,n-1):
        left =0
        for j in range(i-1,-1,-1):
            if A[j] < A[i]:
                left += 1

        right =0
        for j in range(i+1,n):
            if A[j] > A[i]:
                right += 1

        ans += (left * right)

    return ans

# A = [1, 2, 4, 3]
A = [2, 1, 2, 3]
print(solve(A))