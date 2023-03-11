import heapq

def solve(A, B):

    N = len(A)
    heap = []

    for i in range(N):
        for j in range(i + 1, N):
            frac = -(A[i] / A[j])
            if len(heap) == B:
                heapq.heappushpop(heap, (frac, A[i], A[j]))
            else:
                heapq.heappush(heap, (frac, A[i], A[j]))
    ans = heapq.heappop(heap)
    return [ans[1], ans[2]]


def solve1(A,B):

    N = len(A)
    heap = []

    for i in range(N):

        if len(heap) == B:
            heapq.heappushpop(heap, -A[i])
        else:
            heapq.heappush(heap, -A[i])
    ans = heapq.heappop(heap)
    return  - ans


A = [1, 2, 3, 5,6,9,4,-1]
B = 3
print(solve1(A,B))