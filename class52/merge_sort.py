import sys

from class51.Node import Node, print_ll

sys.setrecursionlimit(10000)
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

def middle(A):
    slow = A
    fast = A
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next


    return slow



def merge_sort(A):

    if not A or not A.next :
        return A
    mid = middle(A)
    B = mid.next
    mid.next = None

    A = merge_sort(A)
    B = merge_sort(B)

    return merge(A,B)

head1 = Node(3)
head1.next = Node(4)
head1.next.next = Node(2)
head1.next.next.next = Node(1)
head1.next.next.next.next = Node(8)

print_ll(merge_sort(head1))