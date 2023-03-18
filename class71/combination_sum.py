class Solution:
    def __init__(self):
        self.ans =set()
    def solve(self,i,A,taget,n,B):
        if taget == 0:
            self.ans.add(tuple(B))
            return

        if taget >= A[i]:
            B.append(A[i])
            self.solve(i+1,A,taget-A[i],n,B)
            B.pop()
            self.solve(i + 1, A, taget, n, B)

    def combination(self,A,target):
        A.sort()
        self.solve(0,A,target,len(A),[])
        return sorted(self.ans)

A = [2, 3, 6, 7]
B = 7
A = [ 8, 10, 6, 11, 1, 16, 8 ]
B = 28
A = [10, 1, 2, 7, 6, 1, 5]
B = 8
print(Solution().combination(A,B))