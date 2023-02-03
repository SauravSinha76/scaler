from class51.Node import Node, print_ll

head = Node(1)
head.next = Node(2)
n3 =Node(3)
head.next.next = n3
head.next.next.next =Node(4)
head.next.next.next.next =Node(5)
head.next.next.next.next.next =Node(6)
head.next.next.next.next.next.next =Node(7)
n8 =Node(8)
head.next.next.next.next.next.next.next = n8
n8.next = n3


def remove(A):
    slow = A
    fast = A
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    slow = A
    prv = fast
    while slow != fast:
        prv = fast
        slow = slow.next
        fast = fast.next

    prv.next = None

    return A

print_ll(remove(head))

