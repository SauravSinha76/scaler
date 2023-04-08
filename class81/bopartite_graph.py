import sys


def solve(A, B):
    sys.setrecursionlimit(10**6)
    graph = [[] for _ in range(A)]

    for b in B:
        graph[b[0]].append(b[1])
        graph[b[1]].append(b[0])

    print(graph)

    col = [-1 for _ in range(A)]

    def dfs(src):
        for nbr in graph[src]:
            if col[nbr] == -1:
                col[nbr] = 1 - col[src]
                if not dfs(nbr):
                    return False
            if col[nbr] == col[src]:
                return False
        return True

    for i in range(A):
        if col[i] == -1:
            col[i] = 1
            if not dfs(i):
                return 0
    return 1


A = 2
B = [[0, 1]]

# A = 3
# B = [ [0, 1], [0, 2], [1, 2] ]

A = 10
B = [
    [7, 8],
    [1, 2],
    [0, 9],
    [1, 3],
    [6, 7],
    [0, 3],
    [2, 5],
    [3, 8],
    [4, 8]
]

print(solve(A, B))
