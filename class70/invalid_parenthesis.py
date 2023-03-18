class Solution:
    def __init__(self):
        self.ans =set()
        self.left = 0
        self.right = 0

    def set_offset_count(self,A):
        for a in A:
            if a == '(':
                self.left += 1
            elif a == ')':
                if self.left > 0:
                    self.left -= 1
                else:
                    self.right += 1

        print(self.left)
        print(self.right)

    def param(self, idx, curr_str, s, left, right, balance):
        if idx == len(s):
            if left == 0 and right == 0:
                self.ans.add(curr_str)
        elif balance >= 0:
            if s[idx] == '(' and left > 0:
                self.param(idx + 1, curr_str, s, left - 1, right, balance)
            if s[idx] == ')' and right > 0:
                self.param(idx + 1, curr_str, s, left, right - 1, balance)

            diff = 0

            if s[idx] == ')':
                diff = -1
            if s[idx] == '(':
                diff = 1

            self.param(idx + 1, curr_str + s[idx], s, left, right, balance + diff)

    def solve(self,A):
        self.set_offset_count(A)
        self.param(0,"",A,self.left,self.right,0)
        return list(self.ans)

A = "(())())"
A = "()())()"
A = ")((p"
# A = "()"
s = Solution()
print(s.solve(A))