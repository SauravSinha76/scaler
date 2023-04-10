from collections import deque
from queue import PriorityQueue


def solve(A, B):
    degree = [0] * (A + 1)
    graph = [[] for _ in range(A + 1)]
    for b in B:
        graph[b[0]].append(b[1])
        degree[b[1]] += 1

    print(graph)
    print(degree)
    q = PriorityQueue()

    for i in range(1, A + 1):
        if degree[i] == 0:
            q.put(i)

    print(q)
    ans = []
    while not q.empty():
        edge = q.get()
        ans.append(edge)
        for nbr in graph[edge]:
            degree[nbr] -= 1
            if degree[nbr] == 0:
                q.put(nbr)

    return ans


A = 6
B = [[6, 3],
     [6, 1],
     [5, 1],
     [5, 2],
     [3, 4],
     [4, 2]]

A = 8
B =[
  [1, 4],
  [1, 2],
  [4, 2],
  [4, 3],
  [3, 2],
  [5, 2],
  [3, 5],
  [8, 2],
  [8, 6]
]
# A = 3
# B = [[1, 2],
#      [2, 3],
#      [3, 1]]
print(solve(A, B))
