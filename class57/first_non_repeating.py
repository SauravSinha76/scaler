from class57.MyQueue import MyQueue


def solve(A):

    queue = MyQueue()
    ans = A[0]
    n = len(A)
    queue.enqueue(A[0])
    for i in range(1,n):
        if A[i] == queue.front():
            queue.dequeue()
        else:
            queue.enqueue(A[i])
        if queue.front():
            ans += queue.front()
        else:
            ans += '#'

    return ans

def solve1( A):
    hashMap = {}
    myQueue = MyQueue()
    resultStr = ""

    for char in A:
        if char not in hashMap:
            hashMap[char] = 1
            # if char ocuring for the first time, insert in queue
            myQueue.enqueue(char)
        else:
            hashMap[char] += 1

        while myQueue.front() and hashMap[myQueue.front()] > 1:
            myQueue.dequeue()

        if myQueue.front():
            resultStr += myQueue.front()
        else:
            resultStr += '#'

    return resultStr
A = "abadbc"
# A = "abcabc"
A = "gu"
print(solve1(A))