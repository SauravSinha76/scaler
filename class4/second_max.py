def solve(A):
    n = len(A)
    max_A =A[0]
    max_2 =-1

    for i in range(1,n):
        if max_A < A[i]:
            max_2 = max_A
            max_A = A[i]
        elif max_2 < A[i] and max_A != A[i]:
            max_2 = A[i]
    return max_2

A =[1,2,2,3,4,4]
print(solve(A))