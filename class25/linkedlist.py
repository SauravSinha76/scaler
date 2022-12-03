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

    def solve(self, A):
        while A:
            print(A.val,end=" ")
            A = A.next
        print()

    def find(self, A,B):
        while A:
            if A.val == B:
                return 1
            A = A.next
        return 0

    def insert(self,A,B,C):
        nn = Node(B)
        if C == 0:
            nn.next = A
            A = nn
        else:
            tmp = A
            i =1
            while i < C and tmp.next:
                tmp = tmp.next
                i += 1
            nn.next = tmp.next
            tmp.next = nn
        return A

    def delete(self,A,B):
        if B == 0:
            A = A.next
        else:
            tmp = A
            i =1
            while i < B:
                tmp = tmp.next
                i += 1
            tmp.next = tmp.next.next
        return A

    def reverse(self,A):
        if A == None:
            print("")
            return
        self.reverse(A.next)
        print(A.val,end=" ")

    def find(self,A,B):
        tmp = A
        for i in range(B):
            tmp = tmp.next

        return tmp.val

    def check(self,A):
        previous = A.val
        tmp = A.next
        while tmp.next:
            if previous < tmp.val:
                return 1
            previous = tmp.val
            tmp = tmp.next

        return 0
    def identical(self,A,B):
        while A and B:
            if A.val != B.val:
                return 0
            A = A.next
            B = B.next

        if A or B:
            return 0

        return 1

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(3)

ll1 = LinkedList()
ll1.append(1)
ll1.append(2)
ll1.append(3)
ll1.append(3)
ll1.append(4)

ll.solve(ll.head)
ll1.solve(ll.head)
# print(ll.find(ll.head,5))
# head =ll.insert(ll.head,9,2)
# ll.solve(head)
# head = ll.delete(head,3)
# ll.solve(head)
# ll.reverse(ll.head)
# print(ll.find(ll.head,3))
# print(ll.check(ll.head))
print(ll.identical(ll.head,ll1.head))