def solve(A):
    n = len(A)
    ans =0
    for i in range(30,-1,-1):
        count =0
        for j in range(n):
            if A[j] & 1 << i:
                count += 1

        if count > 1:
            ans |= 1 << i
            for j in range(n):
                if not (A[j] & 1 << i):
                    A[j] =0
    return ans


A = [53, 39, 88]
A = [38, 44, 84, 12]
print(solve(A))