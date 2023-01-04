def solve(A):
    n = len(A)
    i = n-1
    while i > -1:
        if A[i] > A[i-1]:
            A[i], A[i-1] = A[i-1], A[i]
            break
        i -= 1
    if i == -1:
        A[i],A[0] = A[0],A[i]
    return A

def reverse(A,i,j):
    while i < j:
        A[i],A[j] =A[j],A[i]
        i += 1
        j -= 1

def solve1(A):
    n = len(A)
    if n == 2:
        A[0],A[1]= A[1],A[0]
        return A
    i = n-2
    while i >=0 and A[i+1] <= A[i]:
        i -=1


    if i > 0:
        j = n - 1
        while A[j] <= A[i]:
            j -= 1

        A[i], A[j] = A[j], A[i]

    reverse(A,i+1,n-1)
    return A
A = [1,3,2]
# print(solve(A))
print(solve1(A))