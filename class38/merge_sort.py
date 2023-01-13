def merge(L,R,A):
    i = 0
    j = 0
    k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1

def merge_sort(A):
    if len(A) > 1:

        mid = len(A)//2

        L = A[:mid]

        R = A[mid:]

        merge_sort(L)

        merge_sort(R)

        merge(L,R,A)

    return A

A = [9,8,7,6,5,4,3,2,1]
print(merge_sort(A))