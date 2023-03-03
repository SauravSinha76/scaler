import heapq
def solve( A,B):
    sums = 0
    for i in range(len(A)):
        A[i] *= -1
    heapq.heapify(A)
    i = 0
    while len(A) > 1 and i < B:
        x = heapq.heappop(A)
        sums = sums - x
        heapq.heappush(A, -(-x // 2))
        i += 1
    return sums % ((10 ** 9) + 7)

A = 3
B = [6, 5]
A = 10
B = [ 2147483647, 2000000014, 2147483647 ]
print(solve(B,A))