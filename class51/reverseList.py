class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    head = None
    def append(self,x):
        if self.head is None:
            self.head = Node(x)
        else:
            tmp = self.head
            while tmp.next:
                tmp = tmp.next
            tmp.next = Node(x)

    def print(self, A):
        while A:
            print(A.val,end=" ")
            A = A.next
        print()

    def reverse(self,A):


        prv = None
        curr = A

        while curr:
            temp = curr.next

            curr.next = prv
            prv = curr
            curr = temp

        return prv

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

ll.print(ll.head)

ll.print(ll.reverse(ll.head))