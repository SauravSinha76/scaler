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
    min_heap = []
    max_heap= []
    for i in range(n):
        heapq.heappush(min_heap,A[i])
        heapq.heappush(max_heap,-A[i])

    ignore_ele ={}
    for i in range(n):
        min_ele = heapq.heappop(min_heap)
        max_ele = - heapq.heappop(max_heap)
        if min_ele not in ignore_ele and max_ele not in ignore_ele:
            ignore_ele[min_ele] = ignore_ele.get(min_ele, 0) + 1
            ignore_ele[max_ele] = ignore_ele.get(max_ele, 0) + 1
            avg = (min_ele + max_ele) // 2
            min_ele += avg
            max_ele -= avg

            heapq.heappush(min_heap,min_ele)
            heapq.heappush(min_heap, max_ele)
            heapq.heappush(max_heap, -max_ele)
            heapq.heappush(max_heap, - min_ele)


    ans =[]
    for i in range(len(min_heap)):
        if min_heap[i] not in ignore_ele:
            ans.append(A[i])
    return ans

A =[2,2]
A = [3,2,7]
# A =[13,4,10,17,6,16]
# A= [-7,-7,-7,-7,-7]
print(solve(A))
