import heapq


def solve1(A,B):

    heap = []

    for a in A:
        for aa in a:
            if len(heap) == B:
                heapq.heappushpop(heap, -aa)
            else:
                heapq.heappush(heap, -aa)
    ans = heapq.heappop(heap)
    return  - ans

A = [ [9, 11, 15],
       [10, 15, 17] ]
B = 6
A = [[5, 9, 11],
     [9, 11, 13],
     [10, 12, 15],
     [13, 14, 16],
     [16, 20, 21]]
B = 12
print(solve1(A,B))