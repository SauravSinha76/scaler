class Node:
    def __init__(self,x):
        self.val = x
        self.next = None


class MyQueue:

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,x):
        node = Node(x)
        if self.tail:
            self.tail = node
        else:
            self.tail = node
            self.head = node

    def dequeue(self):
        if self.head:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            print("Queue is empty")

    def front(self):
        if self.head:
            return self.head.val
        else:
            print("Queue is empty")
