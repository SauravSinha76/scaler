def solve(A):
    A.sort(reverse=True)
    print(A)
    n = len(A)
    if A[0] == 0:
        return 1
    greater = -1
    for i in range(1,n):
        if A[i] != A[i-1]:
            greater = i

        if A[i] == greater:
            return 1
    return 0

A = [3, 2, 1, 3]
# A = [1, 1, 3, 3]
print(solve(A))