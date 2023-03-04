import heapq
def solve(A,B):
    heapq.heapify(A)

    while B > 0:
        val = heapq.heappop(A)
        heapq.heappush(A, -val)
        B -= 1

    return sum(A)

A = [24, -68, -29, -9, 84]
B = 4
A = [57, 3, -14, -87, 42, 38, 31, -7, -28, -61]
B = 10
print(solve(A,B))
