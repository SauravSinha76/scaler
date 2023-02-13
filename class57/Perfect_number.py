

from queue import Queue
def solve(A):

    queue = Queue()
    queue.put("")
    count = 0
    while count <= A:
        x = queue.get()

        elem1 = x + '1'
        count += 1
        if count == A:
            return elem1+elem1[::-1]
        else:
            queue.put(elem1)

        elem2 = x + '2'
        count += 1
        if count == A:
            return elem2 + elem2[::-1]
        else:
            queue.put(elem2)


print(solve(4))