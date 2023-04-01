def binery_search(low,high,A,target):
    res = 0
    while low <= high:
        mid = (high + low) // 2

        if A[mid] == target:
            return mid
        elif A[mid] < target:
            low = mid+1
        else:
            res = mid
            high = mid -1
    return res


def findLIS(A):
    n = len(A)
    dp =[A[0]]

    for i in range(1,n):
        if A[i] > dp[-1]:
            dp.append(A[i])
        else:
            index = binery_search(0,len(dp)-1, dp,A[i])
            dp[index] = A[i]

    return len(dp)

A= [2, 1, 4, 3]
A= [5, 6, 3, 7, 9]
A = [ 6, 6, 9, 7, 3, 5, 1, 7, 10 ]
print(findLIS(A))