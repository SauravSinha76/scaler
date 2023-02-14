from class57.MyQueue import MyQueue


def solve(A):

    queue = MyQueue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    count = 3
    ans = []
    while count < A:
        x = queue.front()
        queue.dequeue()
        ans.append(x)
        queue.enqueue(x * 10 + 1)
        queue.enqueue(x * 10 + 2)
        queue.enqueue(x * 10 + 3)
        count += 3

    i = len(ans)
    while i < A and queue.head :
        ans.append(queue.head.val)
        queue.head = queue.head.next
        i += 1

    return ans

A = 3
print(solve(A))