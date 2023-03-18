class Solution:
    def __init__(self):
        self.ans =[]

    def subset(self,i,n,A,B):
        self.ans.append(list(B))
        for j in range(i,n):
            if j == i or A[j] != A[j-1]:
                B.append(A[j])
                self.subset(j+1,n,A,B)
                B.pop()

    def solve(self,A):
        n = len(A)
        A.sort()
        self.subset(0,n,A,[])
        return sorted(self.ans)

A = [1, 2, 2]
s = Solution()
print(s.solve(A))
