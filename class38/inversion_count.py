def solve(A):
    n = len(A)
    count =0
    for i in range(n-1):
        for j in range(i+1,n):
            if A[j] < A[i]:
                count += 1

    return count

def merge(A,l,mid,r):
    i = l
    j = mid+1
    C =[]
    inv_count =0
    while i <= mid and j <= r:
        if A[i] <= A[j]:
            C.append(A[i])
            i += 1
        else:
            inv_count += (mid - i +1)
            C.append(A[j])
            j +=1

    while i <= mid:
        C.append(A[i])
        i += 1
    while j <= r:
        C.append(A[j])
        j += 1

    k =0
    for i in range(l, r+1):
        A[i] = C[k]
        k+= 1

    return inv_count

def merge_sort(A,l,r):
    inv_count =0

    if l == r: return 0

    mid = l + (r - l)//2

    inv_count += merge_sort(A,l,mid)
    inv_count += merge_sort(A,mid+1,r)
    inv_count += merge(A,l,mid,r)
    return inv_count


A = [3, 2, 1]
A = [9,8,7,6,5,4,3,2,1]
A = [ 6, 12, 10, 17, 10, 22, 9, 19, 21, 31, 26, 8 ]
print(solve(A))
print(merge_sort(A,0,len(A) -1))
print(A)