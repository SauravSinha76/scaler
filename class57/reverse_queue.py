from class57.MyQueue import MyQueue


def solve(A,B):

    queue = MyQueue()
    stack =[]

    for i in range(B):
        stack.append(A[i])

    while len(stack) != 0:
        queue.enqueue(stack[-1])
        stack.pop()

    for i in range(B,len(A)):
        queue.enqueue(A[i])

    i =0
    while queue.head:
        A[i] = queue.head.val
        queue.head = queue.head.next
        i += 1

    return A

A = [1, 2, 3, 4, 5]
B = 3
print(solve(A,B))

