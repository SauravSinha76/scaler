from class51.Node import Node


def reverse(A):
    prv = None
    curr = A

    while curr:
        temp = curr.next

        curr.next = prv
        prv = curr
        curr = temp

    return prv

def solve(A):

    h1 = A
    slow = A
    fast = A

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    h2 = slow.next
    slow.next = None

    h2 = reverse(h2)

    while h1 and h2:
        if h1.value != h2.value:
            return False
        h1 = h1.next
        h2 = h2.next
    return True



head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(4)

print(solve(head))

