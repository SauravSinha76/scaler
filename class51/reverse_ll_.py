from class51.Node import Node, print_ll


def reverse(A,B,C):
    i = 1
    prv = None
    curr = A
    while curr and i < B:
        prv = curr
        curr = curr.next
        i += 1

    start = prv
    end = curr

    while curr and i <= C:
        tmp = curr.next

        curr.next = prv
        prv = curr
        curr = tmp
        i += 1
    if B == 1:
        A = prv
    else:
        start.next = prv

    end.next = curr
    return A


head = Node(1)
# head.next = Node(2)
# head.next.next =Node(3)
# head.next.next.next =Node(4)
# head.next.next.next.next =Node(5)
print_ll(head)

print_ll(reverse(head,1,1))
