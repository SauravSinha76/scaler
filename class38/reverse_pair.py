def solve(A):
    n = len(A)

    count = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if A[i] > 2* A[j]:
                count += 1

    return count

def merge(A,l,mid,r):

    i =l
    j = mid +1
    rev_count = 0

    while i <= mid:
        while j <= r and A[i] > 2 * A[j]:
            j += 1
        rev_count += j - (mid + 1)
        i += 1

    i =l
    j = mid+1
    C =[]
    while i <= mid and j <= r:
        if A[i] <= A[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(A[j])
            j += 1

    while i <= mid:
        C.append(A[i])
        i += 1

    while j <= r:
        C.append(A[j])
        j += 1

    k =0
    for i in range(l,r+1):
        A[i] = C[k]
        k += 1
    return rev_count

def merge_sort(A,l,r):
    rev_count =0
    if l == r: return 0

    mid = l + (r - l) // 2
    rev_count += merge_sort(A,l,mid)
    rev_count += merge_sort(A,mid+1,r)
    rev_count += merge(A,l,mid,r)
    return rev_count

A = [1, 3, 2, 3, 1]
# A = [4, 1, 2]
print(solve(A))
print(merge_sort(A,0,len(A)-1))