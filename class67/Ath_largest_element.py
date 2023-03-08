import heapq


def solve(A,B):
    heap =[]
    ans= []
    n = len(B)
    i =0
    while i < A:
        heapq.heappush(heap,B[i])
        if i != A -1:
            ans.append(-1)
        i += 1

    ans.append(heap[0])
    while i < n:
        if heap[0] < B[i]:
            heapq.heappushpop(heap, B[i])
        ans.append(heap[0])
        i += 1
    return ans

A = 4
B = [1,2,3,4,5,6]
# A = 2
# B = [15, 20, 99, 1]
print(solve(A,B))


