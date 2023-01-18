def upper_bound(A,ele):
    l = 0
    r = len(A) -1
    while l <= r:
        mid = (l + r) // 2
        if A[mid] == ele:
            return mid
        elif A[mid] > ele:
            r = mid -1
        else:
            l = mid + 1
    return l

def rec_upper_bound(low,high,ele,arr):
    mid = (low + high) // 2

    if low <= high:
        if arr[mid] < ele:
            return rec_upper_bound(mid + 1,high,ele,arr)
        return rec_upper_bound(low,mid -1,ele,arr)
    return low

def solve(A):
    n = len(A)
    m = len(A[0])
    min_val = A[0][0]
    max_val = A[0][m-1]
    for i in range(n):
        min_val = min(min_val,A[i][0])
        max_val = max(max_val,A[i][m-1])


    desired = (m * n)//2
    ans =0
    while min_val <= max_val:
        pos = 0
        mid = (min_val + max_val) // 2
        for i in range(n):
           pos += rec_upper_bound(0,len(A[i])-1, mid,A[i])
        if pos <= desired:
            ans = mid
            min_val = mid + 1
        else:
            max_val = mid - 1

    return ans

A = [
    [1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]
]
print(solve(A))
