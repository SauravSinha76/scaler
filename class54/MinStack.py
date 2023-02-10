class Node:
    def __init__(self,x):
        self.val = x
        self.next = None
        self.next_min = None
class MinStack:
    def __init__(self):
        self.head = None
        self.min_val = None
        self.size =0

    # @param x, an integer
    # @return nothing
    def push(self,x):
        if self.head:
            node = Node(x)
            node.next = self.head
            self.head = node
            if self.min_val and self.min_val.val > x:
                node.next_min = self.min_val
                self.min_val = node
        else:
            self.head = Node(x)
            self.min_val = self.head
        self.size += 1

    # @return nothing
    def pop(self):
        if self.head:
            if self.min_val.val == self.head.val:
                self.min_val = self.min_val.next_min
            self.head = self.head.next
            self.size -= 1
        else:
            return

    # @return an integer
    def top(self):
        if self.head:
            return self.head.val
        else:
            return -1

    # @return an integer
    def getMin(self):
        if self.min_val:
            return self.min_val.val
        else:
            return -1


min_stack = MinStack()
# min_stack.push(1)
# min_stack.push(2)
# min_stack.push(-2)
# print(min_stack.getMin())
# min_stack.pop()
# print(min_stack.getMin())
# print(min_stack.top())

A = "19 P 10 P 9 g P 8 g P 7 g P 6 g p g p g p g p g p g".split()
i = 1
while i < len(A):
    if A[i] == 'P':
        min_stack.push(int(A[i+1]))
        i += 2
    elif A[i] == 'g':
        print(min_stack.getMin())
        i += 1
    elif A[i] == 'p':
        min_stack.pop()
        i += 1
    else:
        print(min_stack.top())
