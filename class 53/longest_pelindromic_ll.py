from class51.Node import Node


def count_length(h1,h2):
    count =0
    while h1 and h2:
        if h1.value == h2.value:
            count += 1
        h1 = h1.next
        h2 = h2.next
    return count
def solve(A):

    curr = A
    prv = None
    ans = 0
    while curr:
        tmp = curr.next

        curr.next = prv


        ans = max(ans, 2 * count_length(prv, tmp))

        ans = max(ans, 2 * count_length(curr, tmp))

        prv = curr
        curr = tmp
    return ans

haed = Node(1)
haed.next = Node(2)
haed.next.next