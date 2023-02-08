class Node:

    def __init__(self,x):
        self.val = x
        self.next = None
        self.prv = None

class Stack:

    def __init__(self):
        self.head = None
        self.middle = None
        self.size = 0


    def push(self,x):
        node = Node(x)
        if self.size <= 0:
            self.head = node
            self.middle = node
        elif self.size <= 1:
            node.prv = self.head
            self.head.next = node
            self.head = node
            self.middle = self.head
        else:
            node.prv = self.head
            self.head.next = node
            self.head = node
            if self.size % 2 == 1:
                self.middle = self.middle.next

        self.size += 1
    def get_middle_value(self):
        if self.middle:
            return self.middle.val
        else:
            return -1

    def delete_middle(self):
        if self.size <= 0:
            return
        elif self.size <= 1:
            self.head = None
            self.middle = None
        else:
            if self.size % 2 == 0:
                self.middle = self.middle.prv
            else:
                self.middle = self.middle.next
        self.size -= 1




    def pop(self):
        if self.size <= 0:
            return -1
        elif self.size <= 1:
            x = self.head.val
            self.head = None
            self.middle = None
        elif self.size <= 2:
            x = self.head.val
            self.head = self.head.prv
            self.head.next = None
            self.middle = self.middle.prv
        else:
            x = self.head.val
            self.head = self.head.prv
            self.head.next = None
            if self.size % 2 == 0:
                self.middle = self.middle.prv
        self.size -= 1
        return x


class Solution:


    def solve(self,A):
        stack = Stack()
        ans =[]
        for a in A:
            if a[0] == 1:
                stack.push(a[1])
            elif a[0] == 2:
                ans.append(stack.pop())
            elif a[0] == 3:
                ans.append(stack.get_middle_value())
            else:
                stack.delete_middle()

        return ans


s = Solution()
A = [
        [1, 3],
        [3, 0],
        [4, 0],
        [2 ,0],
        [1, 5],
        [1, 9],
        [3, 0]
     ]
A = [
        [1, 1],
        [1, 2],
        [1, 3],
        [3, 0],
        [4, 0],
        [3, 0],
        [4, 0]
     ]
A =[
  [2, 0],
  [4, 0],
  [3, 0],
  [1, 170],
  [1, 479],
  [3, 0],
  [3, 0],
  [1, 706],
  [2, 0],
  [2, 0]
]

A =[
  [1, 548],
  [1, 663],
  [2, 0],
  [2, 0],
  [4, 0],
  [4, 0],
  [2, 0],
  [2, 0],
  [3, 0],
  [1, 36]
]
print(s.solve(A))