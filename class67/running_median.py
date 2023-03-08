import heapq


def balance(h1, h2):
    if len(h1) > len(h2):
        val =heapq.heappop(h1)
        heapq.heappush(h2,-val)
    else:
        val = heapq.heappop(h2)
        heapq.heappush(h1, -val)

def solve(A):

    heap1 =[]
    heap2 =[]

    heapq.heappush(heap1, -A[0])
    n = len(A)
    ans =[]
    ans.append(-heap1[0])
    for i in range(1,n):
        if A[i] > - heap1[0]:
            heapq.heappush(heap2,A[i])
        else:
            heapq.heappush(heap1, -A[i])

        diff = abs(len(heap1) - len(heap2))

        if diff == 2:
            balance(heap1,heap2)
        if len(heap1) > len(heap2):
            ans.append(-heap1[0])
        elif len(heap2) > len(heap1):
            ans.append(heap2[0])
        else:
            ans.append(-heap1[0])
    return ans

A = [1, 2, 5, 4, 3]
A = [5, 17, 100, 11]
print(solve(A))