class Node:
    def __init__(self,x):
        self.val = x
        self.right = None
        self.down = None


def merge(A,B):

    dummy = Node(-1)

    tail = dummy
    A.right = B.right

    while A and B:
        if A.val <= B.val:
            tail.down = A
            A = A.down
        else:
            tail.down = B
            B = B.down

        tail = tail.down

    if not A:
        tail.down = B
    if not B:
        tail.down = A

    return dummy.down
def solve(root):

    temp = root

    while temp and temp.right:
        temp = merge(temp,temp.right)

    temp = root
    while temp:
        print(temp.val,end=" ")
        temp = temp.down

    return root

# root = Node(2)
# root.down = Node(7)
# root.down.down = Node(7)
# root.right = Node(4)
# root.right.down = Node(11)

# root = Node(3)
# root.down = Node(7)
# root.down.down = Node(7)
# root.down.down.down = Node(8)
#
# first = Node(4)
# root.right = first
# first.down = Node(11)
#
# second = Node(20)
# first.right = second
# second.down = Node(22)
#
# third = Node(20)
# second.right = third
# third.down = Node(20)
# third.down.down = Node(28)
# third.down.down.down = Node(39)
#
# forth = Node(30)
# third.right = forth
# forth.down = Node(31)
# forth.down.down = Node(39)


root = Node(4)
root.down = Node(7)
root.down.down = Node(13)
root.down.down.down = Node(17)

first = Node(4)
root.right = first
solve(root)
