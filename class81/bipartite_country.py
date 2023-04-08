import sys


def solve(A,B):
    sys.setrecursionlimit(10 ** 6)
    graph = [[] for _ in range(A+1)]

    for b in B:
        graph[b[0]].append(b[1])
        graph[b[1]].append(b[0])

    print(graph)

    col = [-1 for _ in range(A+1)]

    def dfs(src):
        for nbr in graph[src]:
            if col[nbr] == -1:
                col[nbr] = 1 - col[src]
                if not dfs(nbr):
                    return False
            if col[nbr] == col[src]:
                return False
        return True


    col[1] = 1
    dfs(1)
    set1 = 0
    set2 = 0
    for i in range(A+1):
        if col[i] == 1:
            set1 +=1
        elif col[i] == 0:
            set2 +=1
    return (set1 * set2) - len(B)


A = 5
B = [
       [1, 3],
       [1, 4],
       [3, 2],
       [3, 5]
     ]

A = 3
B = [
       [1, 2],
       [1, 3]
     ]

print(solve(A,B))