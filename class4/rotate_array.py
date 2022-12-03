class Reverse:
    def reverse(self,A, B, C):
        while B < C:
            A[B], A[C] = A[C], A[B]
            B += 1
            C -= 1
        return A
    def solve(self,A,B):
        n = len(A)
        B = B % n
        self.reverse(A,0,n-1)
        self.reverse(A,0,n-B-1)
        self.reverse(A,n-B,n-1)
        return A

A =[1,2,3,4,5,6,7]
B = 2
rev = Reverse()
print(rev.solve(A,B))