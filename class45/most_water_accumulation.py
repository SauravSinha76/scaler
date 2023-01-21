def solve(A):
    n = len(A)

    i =0
    j = n-1
    ans =0
    while i < j:
        water = min(A[i],A[j]) * (j - i)
        ans = max(ans,water)

        if A[i] < A[j]:
            i += 1
        else:
            j -= 1
    return ans

A = [1, 5, 4, 3]
A = [1]
print(solve(A))