from class51.Node import Node, print_ll

def add(A,B):
    C = Node(-1)
    head_A = A
    head_B = B
    head_C = C
    carr =0
    while head_A and head_B:
        x = head_A.value + head_B.value + carr
        carr = x // 10
        val = x % 10
        head_C.next = Node(val)
        head_A = head_A.next
        head_B = head_B.next
        head_C = head_C.next

    while head_A:
        x = head_A.value + carr
        carr = x // 10
        val = x % 10
        head_C.next = Node(val)
        head_A = head_A.next
        head_C = head_C.next

    while head_B:
        x = head_B.value + carr
        carr = x // 10
        val = x % 10
        head_C.next = Node(val)
        head_B = head_B.next
        head_C = head_C.next

    if carr != 0:
        head_C.next = Node(carr)

    return C.next
head1 = Node(2)
head1.next = Node(4)
head1.next.next = Node(3)

head2 = Node(5)
head2.next = Node(6)
head2.next.next = Node(4)


head1 = Node(9)
head1.next = Node(9)
# head1.next.next = Node(3)

head2 = Node(1)
# head2.next = Node(6)
# head2.next.next = Node(4)
print_ll(head1)
print_ll(head2)
print_ll(add(head1,head2))