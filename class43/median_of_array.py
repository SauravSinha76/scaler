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
    if m < 1:
        min_val = A[0]
        max_val = A[-1]
    elif n < 1:
        min_val = B[0]
        max_val = B[-1]
    else:
        min_val = min(A[0],B[0])
        max_val = max(A[-1],B[-1])

    desired = (m+n) // 2
    x = get_median(A, B, desired, m, max_val, min_val, n)
    if (m + n) % 2 == 0:
        desired -= 1
        y = get_median(A, B, desired, m, max_val, min_val, n)
        return (x+y)/2
    return float(x)


def get_median(A, B, desired, m, max_val, min_val, n):
    ans =0
    while min_val <= max_val:
        mid = (min_val + max_val) // 2

        pos = count_less_then(0, n - 1, A, mid)
        pos += count_less_then(0, m - 1, B, mid)

        if pos <= desired:
            ans = mid
            min_val = mid + 1
        else:
            max_val = mid -1
    return ans

A = [1, 4, 5]
B = [2, 3]
A = [1, 2, 3]
B = [4]
# A= []
# B=[20]
A = [ 0, 23 ]
B = [  ]
print(solve(A,B))
