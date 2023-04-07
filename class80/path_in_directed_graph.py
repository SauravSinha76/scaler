import sys


def solve(A,B):
    sys.setrecursionlimit(10**6)
    graph =[[] for _ in range(A+1)]

    for b in B:
        graph[b[0]].append(b[1])

    print(graph)

    visited = [False] * (A+1)
    path = [False] *  (A+1)

    def dfs(src):
        visited[src] = True
        path[src] = True
        for nbr in graph[src]:
            if path[nbr]:
                return True
            if not visited[nbr] and dfs(nbr):
                return True
        path[src] = False
        return False

    for i in range(1,A+1):
        if not visited[i] and dfs(i):
            return 1

    return 0

A = 5
B = [[1, 2],
     [4, 1],
     [2, 4],
     [3, 4],
     [5, 2],
     [1, 3]]

A = 5
B = [[1, 2],
     [2, 3],
     [3, 4],
     [4, 5]]
print(solve(A,B))