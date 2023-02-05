class Node:
    def __init__(self,x):
        self.value = x
        self.next = None

head = None

def append( x):
    global head
    if head is None:
        head = Node(x)
    else:
        tmp = head
        while tmp.next:
            tmp = tmp.next
        tmp.next = Node(x)

def insert_node(position, value):
    global head
    if head is None and position == 1:
        head = Node(value)
        return
    temp = head
    i = 1
    while temp.next and i < position-1:
        temp = temp.next
        i += 1
    if temp.next is None:
        temp.next = Node(value)
    else:
        nn = Node(value)
        nn.next = temp.next
        temp.next = nn

def delete_node(position):
    global head
    temp = head
    i = 1
    while temp.next.next and i < position-1:
        temp = temp.next
        i += 1
    if temp.next.next is None:
        temp.next = None
    else:
        temp.next = temp.next.next

def print_ll():
    global head
    temp = head
    while temp:
        if temp.next is None:
            print(temp.value,end="")
        else:
            print(temp.value,end=" ")
        temp = temp.next
    print()

for i in range(1,60):
    insert_node(i,i)
insert_node(5,9)
delete_node(32)

print_ll()