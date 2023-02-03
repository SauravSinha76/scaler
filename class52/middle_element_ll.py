from class51.Node import Node

head = Node(1)
head.next = Node(2)
head.next.next =Node(3)
head.next.next.next =Node(4)
head.next.next.next.next =Node(5)
head.next.next.next.next.next =Node(6)
head.next.next.next.next.next.next =Node(7)
# head.next.next.next.next.next.next.next =Node(8)



def solve(A):
    slow = A
    fast = A
    count = 1
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        count += 2

    if fast.next:
        return slow.next.value
    else:
        return slow.value


print(solve(head))