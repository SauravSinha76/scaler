from class51.Node import Node, print_ll


def reverse(A,B):

    prv = None
    curr = A

    i = 1
    while i <= B:
        tmp = curr.next

        curr.next = prv
        prv = curr
        curr = tmp
        i += 1
    return prv

head = Node(1)
head.next = Node(2)
head.next.next =Node(3)
head.next.next.next =Node(4)
head.next.next.next.next =Node(5)
print_ll(head)

print_ll(reverse(head,2))