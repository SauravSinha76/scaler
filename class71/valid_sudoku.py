import math


class Solution:
    def __init__(self):
        self.n = 0

    def isValid(self,A,row,col,x):

        for k in range(self.n):
            if A[row][k] == x or A[k][col] == x:
                return False
        rrot_n = int(math.sqrt(self.n))
        row = row - row % rrot_n
        col = col - col % rrot_n
        for i in range(rrot_n):
            for j in range(rrot_n):
                if A[row + i][col + j] == x:
                    return False
        return True
    def soduko(self,A,i,j):
        if j == self.n:
            i += 1
            j = 0

        if i == self.n:
            return True

        if A[i][j] != '.':
            if self.soduko(A,i,j+1):
                return True
        else:
            for k in range(1,self.n+1):
                k = f'{k}'
                if self.isValid(A,i,j,k):
                    A[i][j] = k
                    if self.soduko(A,i,j+1):
                        return True
                    A[i][j] = '.'

        return False

    def solve(self,A):
        self.n = len(A)
        for i in range(self.n):
            A[i] = list(A[i])
        self.soduko(A,0,0)

A = [ "53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79" ]


Solution().solve(A)
for a in A:
    print(a)