from class51.Node import Node, print_ll


def reverse(A):
    j = True
    start = A
    prv_start = start
    head = None
    curr = start
    while curr :
        prv = None

        curr = start

        i = 1
        while i <= 2:
            if curr:
                tmp = curr.next

                curr.next = prv
                prv = curr
                curr = tmp
            i += 1
        if j :
            head = prv
            j = False
        else:
            prv_start.next = prv
            prv_start = start
        start = curr
    return head

head = Node(1)
head.next = Node(2)
head.next.next =Node(3)
head.next.next.next =Node(4)
head.next.next.next.next =Node(5)
head.next.next.next.next.next =Node(6)
print_ll(head)

print_ll(reverse(head))