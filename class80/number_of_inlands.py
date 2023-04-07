def solve(A):
    n = len(A)
    m = len(A[0])
    dx =[-1,1,0,0,1,-1,-1,1]
    dy =[0,0,-1,1,1,-1,1,-1]
    def bfs(x,y):
        if x < 0  or x >= n or  y < 0 or y >= m or  A[x][y] == 0 :
            return
        if A[x][y] == 1:
            A[x][y] = 0
            for i in range(len(dx)):
                bfs(x+dx[i],y+dy[i])
    count =0
    for i in range(n):
        for j in range(m):
            if A[i][j] == 1:
                bfs(i,j)
                count +=1

    return count

A = [
       [0, 1, 0],
       [0, 0, 1],
       [1, 0, 0]
     ]

A = [
       [1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [1, 0, 0, 1, 1],
       [0, 0, 0, 0, 0],
       [1, 0, 1, 0, 1]
     ]
print(solve(A))