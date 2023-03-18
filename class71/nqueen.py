class Solution:
    def __init__(self):
        self.ans =[]
        self.n =0

    def isQueenSafe(self,A,row,col):
        for k in range(row):
            if A[k][col] == 'Q':
                return False
        i = row
        j = col

        while i > -1 and j > -1:
            if A[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        i = row
        j = col
        while i >-1 and j < self.n:
            if A[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def nQueen(self,A,row):
        if row == self.n:
            curr_ans =[]
            for i in range(self.n):
                curr_ans.append(''.join(A[i]))
            self.ans.append(list(curr_ans))

        for col in range(self.n):
            if self.isQueenSafe(A,row,col):
                A[row][col] = 'Q'
                self.nQueen(A,row +1)
                A[row][col] = '.'

    def nqueen_opt(self,A,row,cols,diag,anti_diag):
        if row == self.n:
            curr_ans =[]
            for i in range(self.n):
                curr_ans.append(''.join(A[i]))
            self.ans.append(list(curr_ans))

        for col in range(self.n):
            if not cols[col] and not anti_diag[row + col] and not diag[row - col + self.n -1]:
                A[row][col] = 'Q'
                cols[col] = True
                anti_diag[row + col] = True
                diag[row - col + self.n - 1] = True
                self.nqueen_opt(A,row +1,cols,diag,anti_diag)
                A[row][col] = '.'
                cols[col] = False
                anti_diag[row + col] = False
                diag[row - col + self.n - 1] = False

    def solve_opt(self,n):
        self.n = n
        A =[['.' for _ in range(n)]
            for _ in range(n)]
        cols = [False] * self.n
        diag =[False] * (2 * self.n +1)
        anti_diag = [False] * (2 * self.n + 1)
        self.nqueen_opt(A,0, cols, diag, anti_diag)
        return self.ans

    def solve(self,n):
        self.n = n
        A =[['.' for _ in range(n)]
            for _ in range(n)]
        self.nQueen(A,0)
        return self.ans

ans = Solution().solve(4)
for a in ans:
    print(a)
ans = Solution().solve_opt(4)
for a in ans:
    print(a)