def solve(A,B):
    A.sort()
    n = len(A)
    cur_sum = 0
    k = 0
    cur_sum += A[n-1]
    while cur_sum <= B:
        k += 1
        cur_sum += A[n-k-1]

    return k


def func(A, B):
    # Variable declaration
    n = len(A)
    ans = n
    sum = 0
    start = 0

    # Loop till N
    for end in range(n):

        # Sliding window from left
        sum += A[end]

        while sum > B:

            # Sliding window from right
            sum -= A[start]
            start += 1

            # Storing sub-array size - 1
            # for which sum was greater than k
            ans = min(ans, end - start + 1)

            # Sum will be 0 if start>end
            # because all elements are positive
            # start>end only when arr[end]>k i.e,
            # there is an array element with
            # value greater than k, so sub-array
            # sum cannot be less than k.
            if sum == 0:
                break

        if sum == 0:
            ans = -1
            break

    return ans

def check(A,B,mid):
    n = len(A)
    max_sum = 0
    sum = 0
    for i in range(mid):
        sum += A[i]

    max_sum = sum

    start = 0
    end = mid

    while end < n:

        sum += (A[end] - A[start])

        max_sum = max(max_sum,sum)
        start += 1
        end += 1


    if max_sum <= B:
        return True
    else:
        return False
def solve_bs(A,B):
    n = len(A)
    low =1
    high = n-1
    ans = 1
    while low <= high:
        mid = (low + high) // 2

        if check(A,B,mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

# A = [1, 2, 3, 4, 5]
# B = 10
A = [130,5, 17, 100, 11]
B = 130
# A = [ 2, 24, 38, 25, 35, 33, 43, 12, 49, 35, 45, 47, 5, 33 ]
# B = 249
print(func(A,B))
print(solve_bs(A,B))

