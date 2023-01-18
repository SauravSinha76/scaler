def find_pivote(A,low,high):
    if high < low:
        return -1
    if high == low:
        return low

    mid = (low + high) // 2

    if mid < high and A[mid] > A[mid +1]:
        return mid
    if mid > low and A[mid] < A[mid-1]:
        return mid -1
    if A[low] >= A[mid]:
        return find_pivote(A,low,mid-1)
    return find_pivote(A,mid +1, high)


def binery_serach(A,low,high,k):
    mid = (low + high)// 2

    if low <= high:
        if A[mid] == k:
            return mid
        if A[mid] <= k:
            return binery_serach(A,mid + 1,high,k)
        else:
            return binery_serach(A,low,mid-1,k)
    return -1

def pivoted_binery_search(A,k):
    low =0
    high = len(A) -1
    pivote = find_pivote(A,low,high)

    if pivote == -1:
        return binery_serach(A,low,high,k)

    if A[pivote] == k:
        return pivote
    if A[0] < k:
        return binery_serach(A,low,pivote-1,k)
    return binery_serach(A,pivote+1,high,k)

A = [ 1, 7, 67, 133, 178 ]
B = 1
print(pivoted_binery_search(A,B))
