def sort(A):

    n = len(A)

    for i in range(n-1):
        min_val = A[i]
        min_idx = i
        for j in range(i+1,n):
            if min_val > A[j]:
                min_val = A[j]
                min_idx = j

        if min_idx != i:
            A[i],A[min_idx] = A[min_idx],A[i]
    return A

A =[98,76,7,34,79,5,66,23,12]
print(sort(A))