import heapq


def solve(A,B,C):
    min_heap = list(C)
    heapq.heapify(min_heap)
    min_cost = 0
    max_cost = 0
    max_heap = list(map(lambda x: x * -1, C))
    for i in range(A):
        min_val =heapq.heappop(min_heap)
        min_cost += min_val
        min_val -= 1
        if min_val > 0:
            heapq.heappush(min_heap,min_val)

        max_val = - heapq.heappop(max_heap)
        max_cost += max_val
        max_val -= 1
        if max_val > 0:
            heapq.heappush(max_heap, - max_val)

    return [max_cost,min_cost]

A = 4
B = 3
C = [2, 1, 1]
A = 4
B = 3
C = [2, 2, 2]
print(solve(A,B,C))

