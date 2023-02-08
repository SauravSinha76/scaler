from class51.Node import Node, print_ll


def solve(A,B):

    small_head = None
    small_tail = None
    greater_head = None
    greater_tail = None
    c = A
    while c:
        if c.value < B:
            if small_tail:
                small_tail.next = c
                small_tail = small_tail.next
            else:
                small_tail = c
                small_head = small_tail
        else:
            if greater_tail:
                greater_tail.next = c
                greater_tail = greater_tail.next
            else:
                greater_tail = c
                greater_head = greater_tail
        c = c.next
    if greater_tail:
        greater_tail.next = None

    if small_tail:
        small_tail.next = greater_head
    else:
        small_head = greater_head

    return small_head

head = Node(1)
head.next = Node(4)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(2)

print_ll(head)
print_ll(solve(head,3))



