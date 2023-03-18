import sys


class Solution:
    def solve(self, mat):
        self.count = 0

        start_point = [0, 0]
        empty = 1
        row, col = len(mat), len(mat[0])
        # find start point and empty blocks
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1:
                    start_point[0] = i
                    start_point[1] = j
                elif mat[i][j] == 0:
                    empty += 1

        def rateinMaze(i, j, mat, empty):
            if i < 0 or i >= row or j < 0 or j >= col:
                return False

            if mat[i][j] == -1:
                return False

            if mat[i][j] == 2:
                if empty == 0:  # walked every 0 atleast ones
                    self.count += 1
                return

            mat[i][j] = -1  # visited

            rateinMaze(i + 1, j, mat, empty - 1)
            rateinMaze(i - 1, j, mat, empty - 1)
            rateinMaze(i, j + 1, mat, empty - 1)
            rateinMaze(i, j - 1, mat, empty - 1)

            mat[i][j] = 0  # un-visited

        rateinMaze(start_point[0], start_point[1], mat, empty)

        return self.count

A = [   [ 0,  0,  1,  -1,  0,  0,  0],
        [ 0, -1,  0,  -1,  0, -1,  0],
        [ 0, -1,  0,   0, -1,  0,  0],
        [ 0,  0, -1,   0, -1,  0, -1],
        [-1,  0, -1,   0,  0,  0,  0],
        [ 0,  0,  0,  -1,  0, -1,  2]
        ]
A = [   [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 2, -1]   ]
print(Solution().solve(A))