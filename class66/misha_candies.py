import heapq
def solve( A,B):
    sums = 0
    heapq.heapify(A)
    while len(A) > 1 and A[0] <=B:
        x = heapq.heappop(A)
        half = x // 2
        sums = sums + half
        if len(A) > 1:
            y = heapq.heappop(A)
            y += (x - half)
            heapq.heappush(A, y)

    return sums

A = [3, 2, 3]
B = 4
# A = [1, 2, 1]
# B = 2
print(solve(A,B))
