class Solution:
    # @param A : string
    # @return a list of list of strings
    def __init__(self):
        self.mem = []

    def isPalindrome(self, letter):
        return letter == letter[::-1]

    def rec(self, A, temp):
        if len(A) == 0:
            b = temp.copy()
            self.mem.append(b)
            return
        for i in range(len(A)):
            if self.isPalindrome(A[:i + 1]):
                temp.append(A[:i + 1])
            else:
                continue
            self.rec(A[i + 1:], temp)
            temp.pop()

    def partition(self, A):
        self.rec(A, [])
        return self.mem


A = "aab"
s = Solution()
print(s.partition(A))

