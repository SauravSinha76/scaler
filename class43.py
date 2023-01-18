def count_less_then(low,high,A,ele):
    mid = (low + high) // 2
    if low <= high:
        if A[mid] < ele:
            return count_less_then(mid + 1, high,A,ele)
        return count_less_then(low, mid - 1,A, ele)
    return low

def solve(A,B):
    n = len(A)
    m = len(B)
    min_val = min(A[0],B[0])
    max_val = max(A[-1],B[-1])

    desired = (len(A) + len(B)) // 2
    while min_val <= max_val:
        mid = (min_val + max_val) // 2

        pos = count_less_then(0,n-1,A,mid)
        pos += count_less_then(0,m-1,B,mid)

        if pos < desired:
            min_val = mid + 1
        else:
            max_val = mid - 1

    return min_val


A = [1, 4, 5]
B = [2, 3]
A = [1, 2, 3]
B = [4]
print(solve(A,B))
