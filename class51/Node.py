class Node:
    def __init__(self,x):
        self.value = x
        self.next = None

def print_ll(head):
    temp = head
    while temp:
        print(temp.value,end=" ")
        temp = temp.next
    print()