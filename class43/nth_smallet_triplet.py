def binerySearch(low,high,A,ele):
    mid = (low + high) // 2
    if low <= high:
        if A[mid] < ele:
            return binerySearch(mid + 1, high,A,ele)
        return binerySearch(low, mid - 1,A, ele)
    return low

def count_less_then(A,ele):
    n = len(A)
    count =0
    for i in range(n-2):
        for j in range(i+1,n-1):
            val = ele - (A[i]+ A[j])
            right = binerySearch(j+1,n-1,A,val)
            count += right -(j+1)
    return count

def solve(A,B):
    A.sort()
    n = len(A)
    min_val = 1
    max_val = A[n-1] + A[n-2] + A[n-3]
    ans = 0
    while min_val <= max_val:
        mid = (min_val + max_val) // 2

        pos = count_less_then(A, mid)

        if pos < B:
            ans = mid
            min_val = mid + 1
        else:
            max_val = mid - 1
    return ans

A = [2, 4, 3, 2]
B = 3
# A = [1, 5, 7, 3, 2]
# B = 9
print(solve(A,B))
