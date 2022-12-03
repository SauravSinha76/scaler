def solve(A):
    n = len(A)
    max = A[0]
    total =0
    for i in range(1,n):
        if max < A[i]:
            max_2 =max
            max = A[i]
            total += (max - max_2) *i
        else:
            total += max - A[i]
    return total


# A = [3,1,2]
A =[5,5,1,6]
print(solve(A))