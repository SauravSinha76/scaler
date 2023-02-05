class Node:
    def __init__(self,x):
        self.label = x
        self.next = None
        self.random = None

class LinkList:
    head = None

    def append(self, x):
        if self.head is None:
            self.head = Node(x)
        else:
            tmp = self.head
            while tmp.next:
                tmp = tmp.next
            tmp.next = Node(x)

    def print(self, A):
        while A:
            print(A.label,end=" ")
            A = A.next
        print()
    # def insertAtEnd(self,head):

    def reverse(self,head):
        hm = {}
        temp = head
        new_head = Node(temp.label)
        hm[temp] = new_head
        while temp.next:
            new_head.next = Node(temp.next.label)
            new_head = new_head.next
            temp = temp.next
            hm[temp] = new_head
        temp = head
        while temp:
            hm[temp].random = hm.get(temp.random,None)
            temp = temp.next

        return hm[head]


ll = LinkList()
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.arbit = head.next.next
head.next.random = head
head.next.next.random = head.next.next.next.next
head.next.next.next.random = head.next.next
head.next.next.next.next.random = head.next

ll.print(head)
head = ll.reverse(head)
ll.print(head)