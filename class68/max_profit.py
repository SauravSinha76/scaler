import heapq


def solve(A,B):
    n = len(A)

    pair =[]

    for i in range(n):
        pair.append((A[i],B[i]))

    pair.sort()

    heap =[]
    T = 0

    for i in range(n):
        if T < pair[i][0]:
            heapq.heappush(heap,pair[i][1])
            T += 1
        elif pair[i][1] > heap[0]:
            heapq.heappushpop(heap,pair[i][1])

    return sum(heap)

A = [1, 3, 2, 3, 3]
B = [5, 6, 1, 3, 9]
A = [3, 8, 7, 5]
B = [3, 1, 7, 19]
print(solve(A,B))



