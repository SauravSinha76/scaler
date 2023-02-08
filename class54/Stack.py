class Node:
    def __init__(self,x):
        self.val = x
        self.next = None

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0


    def push(self,x):
        node = Node(x)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            self.top = self.top.next
            self.size -= 1
        else:
            print("Stack is empty")

    def top_ele(self):
        if self.top:
            return self.top.val
        else:
            print("Stack is empty")
            return -1

