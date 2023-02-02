from class51.Node import Node, print_ll

def remove_duplicate(A):
    temp = A
    while temp and temp.next:
        while temp.next and temp.value == temp.next.value:
            temp.next = temp.next.next
        temp = temp.next
    return A
head = Node(1)
head.next = Node(1)
head.next.next =Node(1)
head.next.next.next =Node(1)
head.next.next.next.next =Node(1)
print_ll(head)
print_ll(remove_duplicate(head))