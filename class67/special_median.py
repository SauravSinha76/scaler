import heapq


def balance(h1, h2):
    if len(h1) > len(h2):
        val =heapq.heappop(h1)
        heapq.heappush(h2,-val)
    else:
        val = heapq.heappop(h2)
        heapq.heappush(h1, -val)

def solve(A):
    heap1 = []
    heap2 = []

    heapq.heappush(heap1, -A[0])
    n = len(A)
    for i in range(1, n):
        if len(heap1) > len(heap2):
            if -heap1[0] == A[i]:
                return 1
        elif len(heap2) > len(heap1):
            if heap2[0] == A[i]:
                return 1
        else:
            temp = (-heap1[0] + heap2[0]) / 2
            if int(temp) == A[i] and temp - int(temp) == 0.0:
                return 1
        if A[i] > - heap1[0]:
            heapq.heappush(heap2, A[i])
        else:
            heapq.heappush(heap1, -A[i])

        diff = abs(len(heap1) - len(heap2))

        if diff == 2:
            balance(heap1, heap2)

    heap1 = []
    heap2 = []

    heapq.heappush(heap1, -A[n-1])
    for i in range(n-2, -1,-1):
        if len(heap1) > len(heap2):
            if -heap1[0] == A[i]:
                return 1
        elif len(heap2) > len(heap1):
            if heap2[0] == A[i]:
                return 1
        else:
            temp = (-heap1[0] + heap2[0]) / 2
            if int(temp) == A[i] and temp - int(temp) == 0.0:
                return 1
        if A[i] > - heap1[0]:
            heapq.heappush(heap2, A[i])
        else:
            heapq.heappush(heap1, -A[i])

        diff = abs(len(heap1) - len(heap2))

        if diff == 2:
            balance(heap1, heap2)
    return 0

A = [4, 6, 8, 4]
print(solve(A))

