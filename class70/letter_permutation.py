class Solution:
    def __init__(self):
        self.letter_map ={
            '0' : ['0'],
            '1' : ['1'],
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y','z']
        }


    def solve(self,A):
        ans = [""]
        n = len(A)
        for i in range(n):
            c = []
            temp = self.letter_map[A[i]]
            for a in ans:
                for b in temp:
                  c.append(a + b)
            ans = c
        return ans


A = "23"
A = "23456789"
print(Solution().solve(A))