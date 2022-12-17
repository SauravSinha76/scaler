def solve(A):
    ans =0
    for i in range(32):
        count =0
        for j in range(len(A)):
            if A[j] >> i & 1:
                count += 1

        if count % 3 != 0:
            ans += 1 << i
    return ans

A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
print(solve(A))