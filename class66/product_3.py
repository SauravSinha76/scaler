import heapq


def solve(A):
    ans =[-1,-1]
    if len(A) < 2:
        return [-1] * len(A)
    p = A[0] * A[1] * A[2]
    heap = [A[0],A[1],A[2]]
    heapq.heapify(heap)
    ans.append(p)
    for i in range(3, len(A)):
        if heap[0] < A[i]:
            p *= A[i]
            heapq.heappush(heap, A[i])
            val = heapq.heappop(heap)
            p //= val
            ans.append(p)
        else:
            ans.append(p)

    return ans

# A = [1, 2, 3, 4, 5]
# A = [10, 2, 13, 4]
A = [ 11, 5, 6, 2, 8, 10 ]
print(solve(A))
