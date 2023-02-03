from class51.Node import Node, print_ll


def merge(A,B):

    dummy = Node(-1)

    tail = dummy

    while A and B:
        if A.value < B.value:
            tail.next = A
            A = A.next
        else:
            tail.next = B
            B = B.next

        tail = tail.next

    if not A:
        tail.next = B
    if not B:
        tail.next = A

    return dummy.next


head1 = Node(2)
head1.next = Node(6)
head1.next.next = Node(10)
head1.next.next.next = Node(14)
head1.next.next.next.next = Node(19)

head2 = Node(3)
head2.next = Node(5)
head2.next.next = Node(9)
head2.next.next.next = Node(11)


print_ll(head1)
print_ll(head2)
print_ll(merge(head1,head2))