import heapq


def solve(A,B):
    n = len(A)
    i =0
    heap =[]
    ans = []
    while i < B+1:
        heapq.heappush(heap,A[i])
        i += 1

    while i < n:
        ans.append(heapq.heappop(heap))
        heapq.heappush(heap,A[i])
        i += 1
    while len(heap) > 0:
        ans.append(heapq.heappop(heap))
    return ans

A = [1, 40, 2, 3]
B = 2
A = [2, 1, 17, 10, 21, 95]
B = 1
print(solve(A,B))
