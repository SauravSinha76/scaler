

class Node:
    def __init__(self,x):
        self.val = x
        self.next = None

def merge(A):

    dummy = Node(-1)

    tail = dummy

    B = dummy.next
    for i in range(0,len(A)):
        C = A[i]
        while B and C:
            if B.val < C.val:
                tail.next = B
                B = B.next
            else:
                tail.next = C
                C = C.next

            tail = tail.next

        if not B:
            tail.next = C
        if not C:
            tail.next = B

        B =  dummy.next
        tail = dummy
    return dummy.next

ll_1 = Node(1)
ll_1.next = Node(10)
ll_1.next.next = Node(20)

ll_2 = Node(4)
ll_2.next = Node(11)
ll_2.next.next = Node(13)

ll_3 = Node(3)
ll_3.next = Node(8)
ll_3.next.next = Node(9)

A = [ll_1, ll_2, ll_3]
head = merge(A)
while head:
    print(head.val)
    head = head.next