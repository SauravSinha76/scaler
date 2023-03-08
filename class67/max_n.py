import heapq


def solve(A,B):
    n= len(A)
    heap =[]
    for a in A:
        for b in B:
         heap.append(a + b)
    heap.sort(reverse=True)
    return heap[:n]

def solev1(A,B):
    A.sort(reverse=True)
    B.sort(reverse=True)

    N = len(A)
    max_heap = []
    i, j = 0, 0
    heapq.heappush(max_heap, (-(A[i] + B[i]), [i, j]))

    ans = []

    indexSet = set()

    while len(ans) < N:
        cur_max, indx = heapq.heappop(max_heap)

        ans.append(-cur_max)
        i, j = indx[0], indx[1]

        # check cross pairs (i,j+1) and (i+1,j)

        if i < len(A) and j + 1 < len(B):
            if (i, j + 1) not in indexSet:
                indexSet.add((i, j + 1))
                heapq.heappush(max_heap, (-(A[i] + B[j + 1]), [i, j + 1]))

        if i + 1 < len(A) and j < len(B):
            if (i + 1, j) not in indexSet:
                indexSet.add((i + 1, j))
                heapq.heappush(max_heap, (-(A[i + 1] + B[j]), [i + 1, j]))

    return ans
A = [1, 4, 2, 3]
B = [2, 5, 1, 6]

A = [ 3, 2, 4, 2 ]
B = [ 4, 3, 1, 2 ]
print(solve(A,B))
print(solev1(A,B))
