from collections import deque


def solve(A):
    n = len(A)
    m = len(A[0])
    q = deque()
    ans =[[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if A[i][j] == 1:
                q.append((i,j))

    t = 0
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    while q:
        x = len(q)
        for i in range(x):
            pair = q.popleft()
            ans[pair[0]][pair[1]] = t
            for k in range(4):
                ni = pair[0] + dx[k]
                nj = pair[1] + dy[k]
                if -1 < ni < n and -1 < nj < m and A[ni][nj] == 0:
                    A[ni][nj] = 1
                    q.append((ni,nj))

        t += 1
    return ans

A = [
       [0, 0, 0, 1],
       [0, 0, 1, 1],
       [0, 1, 1, 0]
     ]
print(solve(A))