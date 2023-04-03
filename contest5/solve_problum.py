import heapq


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
def solve(A):
    n = len(A)
    heapq.heapify(A)
    for i in range(n):
        print(heapq.heappop(A))
    return A

A =[2,2]
# A = [3,2,7]
A =[13,4,10,17,6,16]
# A= [-7,-7,-7,-7,-7]
print(solve(A))
