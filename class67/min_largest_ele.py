import heapq


def solve(A,B):

    n = len(A)
    curr =[]
    heap =[]
    for i in range(n):
        curr.append(A[i])
        heapq.heappush(heap, ((A[i] + A[i]),i))

    i = 0
    while i < B:
        val, index = heapq.heappop(heap)

        curr[index] += A[index]

        val += A[index]
        heapq.heappush(heap, (val,index))
        i += 1
    return max(curr)

A = [1, 2, 3, 4]
B = 3
A = [5, 1, 4, 2]
B = 5
print(solve(A,B))
