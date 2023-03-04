class Solution:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        i = len(self.heap) -1

        while i > 0:
            pi = (i - 1) // 2
            if self.heap[pi] > self.heap[i]:
                self.heap[pi], self.heap[i] = self.heap[i], self.heap[pi]
                i = pi
            else:
                break

    def heapify(self, i):
        size = len(self.heap)

        while (2 * i) + 1 < size:
            x = min(self.heap[i], self.heap[(2* i)+ 1])
            if size < (2*i) + 2:
                x = min(x , self.heap[(2*i) + 2])
            if x == self.heap[i]:
                break
            elif x == self.heap[(2* i)+ 1]:
                self.heap[i], self.heap[(2* i)+ 1] = self.heap[(2* i)+ 1] , self.heap[i]
                i = (2* i)+ 1
            else:
                self.heap[i], self.heap[(2 * i) + 2] = self.heap[(2 * i) + 2], self.heap[i]
                i = (2 * i) + 2

    def remove(self):
        ans = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.heapify(0)
        return ans


    def solve(self,A):
        for a in A:
            self.insert(a)
        print(self.heap)
        ans = 0
        while len(self.heap) > 1:
            cost = self.remove() + self.remove()
            self.insert(cost)
            ans += cost
        return ans

import heapq
def solve( A):
    sums = 0
    heapq.heapify(A)
    while len(A) > 1:
        x = heapq.heappop(A)
        y = heapq.heappop(A)
        sums = sums + x + y
        heapq.heappush(A, x + y)
    return sums

A = [1, 2, 3, 4, 5]
# # A = [5, 17, 100, 11]
A = [ 16, 7, 3, 5, 9, 8, 6, 15 ]
print(Solution().solve(A))
print(solve(A))