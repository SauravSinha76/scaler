from class51.Node import Node, print_ll


def solve(A):
    hm ={}
    temp = A
    i = 1
    while temp:
        hm[i] = temp
        i += 1
        temp = temp.next

    mid = i // 2
    j= 1
    while j < mid:
        hm[j].next = hm[i - j]
        hm[j].next.next = hm[j + 1]
        j += 1

    if i % 2 == 0:
        hm[j].next = None
    else:
        hm[j].next.next = None
    return A

head = Node(1)
head.next = Node(2)
head.next.next =Node(3)
head.next.next.next =Node(4)
head.next.next.next.next =Node(5)
head.next.next.next.next.next =Node(6)

print_ll(head)
print_ll(solve(head))