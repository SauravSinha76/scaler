class Solution:
    def solve(self,A):
        N = len(A)
        for i in range(1,N):
            A[i][0] += A[i-1][0]

        for i in range(1,N):
            for j in range(1,len(A[i])):
                if i == j:
                    A[i][j] += A[i-1][j-1]
                else:
                    A[i][j] += min(A[i-1][j-1],A[i-1][j])

        return min(A[-1])


s = Solution()
A = [
         [2],
        [3, 4],
       [6, 5, 7],
      [4, 1, 8, 3]
    ]
print(s.solve(A))