import sys


def solve(A,B,C,D):
    sys.setrecursionlimit(10**6)
    visited = [False] * (A + 1)
    adj = [[] for _ in range(A + 1)]

    for u, v in C:
        adj[u].append(v)
        adj[v].append(u)

    def dfs(node, adj):
        visited[node] = True

        total_sum = 0
        total_sum += B[node - 1]

        for child in adj[node]:
            if not visited[child]:
                total_sum += dfs(child, adj)
                visited[child] = True

        return total_sum

    total_batches = 0
    # graph traversal
    for node in range(1, A + 1):
        if not visited[node]:
            batch_strength = dfs(node, adj)

            if batch_strength >= D:
                total_batches += 1

    return total_batches

A = 7
B = [1, 6, 7, 2, 9, 4, 5]
C = [  [1, 2],
        [2, 3],
       [5, 6],
        [5, 7]  ]
D = 12

A = 5
B = [1, 2, 3, 4, 5]
C = [[1, 5],
     [2, 3]]
D = 6

A = 14
B = [ 7, 5, 7, 3, 9, 4, 4, 6, 3, 1, 4, 8, 7, 6 ]
C = [
  [1, 2],
  [2, 6],
  [2, 7],
  [4, 13],
  [5, 8],
  [5, 13],
  [6, 12],
  [7, 10],
  [10, 14],
  [13, 14]
]
D = 2
print(solve(A,B,C,D))