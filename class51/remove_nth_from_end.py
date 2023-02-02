from class51.Node import Node, print_ll


def remove(A,B):
    temp = A
    count = 1
    while temp:
        temp = temp.next
        count += 1

    if B >= count-1:
        A = A.next
        return A

    index = count - B
    i = 1
    temp = A
    while i < index-1:
        temp = temp.next
        i += 1
    temp.next = temp.next.next
    return A
head = Node(1)
head.next = Node(2)
head.next.next =Node(3)
head.next.next.next =Node(4)
head.next.next.next.next =Node(5)
print_ll(head)
print_ll(remove(head,6))