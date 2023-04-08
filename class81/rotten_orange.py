from collections import deque


def solve(A):
    n = len(A)
    m = len(A[0])
    q = deque()

    for i in range(n):
        for j in range(m):
            if A[i][j] == 2:
                q.append((i,j))

    t = 1
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    while q:
        x = len(q)
        for i in range(x):
            pair = q.popleft()
            for k in range(4):
                ni = pair[0] + dx[k]
                nj = pair[1] + dy[k]
                if -1 < ni < n and -1 < nj < m and A[ni][nj] == 1:
                    A[ni][nj] = 2
                    q.append((ni,nj))

        t += 1

    for i in range(n):
        for j in range(m):
            if A[i][j] == 1:
                return -1
    return t-1

A = [   [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]   ]
print(solve(A))
