class Node:
    def init(self, x, next_node=None, prev_node=None):
        self.val = x
        self.next_node = next_node
        self.prev_node = prev_node


class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        head = None
        middle = None
        i = 0
        size = 0
        res = []
        while i < len(A):
            op_type = A[i][0]
            val = A[i][1]

            # add element
            # if size changes from odd to even 1-2-3-4-5 -> 1-2-3-4-5-6, middle = next
            # if size changes from even to odd 1-2-3-4 -> 1-2-3-5-6, dont do anything
            if op_type == 1:
                if size <= 0:
                    head = Node(val)
                    middle = head
                elif size <= 1:
                    temp = head
                    head = Node(val)
                    head.prev_node = temp
                    temp.next_node = head
                    middle = head
                else:
                    temp = head
                    head = Node(val)
                    head.prev_node = temp
                    temp.next_node = head
                    if size % 2 == 1:
                        middle = middle.next_node
                size += 1

            # pop top element
            # if size changes from odd to even 1-2-3-4-5 -> 1-2-3-4, dont do anything
            # if size changes from even to odd 1-2-3-4 -> 1-2-3, move middle to previous
            elif op_type == 2:
                if size <= 0:
                    head = None
                    middle = None
                    res.append(-1)
                elif size <= 1:
                    res.append(head.val)
                    head = None
                    middle = None
                elif size <= 2:
                    res.append(head.val)
                    head = head.prev_node
                    middle = head
                else:
                    res.append(head.val)
                    if size % 2 == 0:
                        middle = middle.prev_node
                    head = head.prev_node
                    head.next_node = None
                size -= 1
                size = max(0, size)

            # return middle element from stack
            elif op_type == 3:
                if size < 1:
                    res.append(-1)
                else:
                    res.append(middle.val)

            # delete middle element
            # if size changes from odd to even 1-2-3-4-5 -> 1-2-4-5, move middle to next
            # if size changes from even to odd 1-2-3-4 -> 1-2-4, move middle to previous
            elif op_type == 4:
                if size <= 1:
                    head = None
                    middle = None
                elif size == 2:
                    head = head.prev_node
                    middle = head
                    head.next_node = None
                elif size > 2:
                    prev = middle.prev_node
                    nxt = middle.next_node
                    prev.next_node = nxt
                    nxt.prev_node = prev
                    if size % 2 == 0:
                        middle = prev
                    else:
                        middle = nxt
                size -= 1
                size = max(0, size)

            i += 1
        return res