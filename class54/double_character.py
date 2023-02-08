from class54.Stack import Stack


def solve(A):

    stack = Stack()

    for a in A:
        if stack.size != 0 and stack.top_ele() == a:
            stack.pop()
        else:
            stack.push(a)

    tmp = stack.top
    arr = []
    while tmp:
        arr.append(tmp.val)
        tmp = tmp.next

    i = 0
    j = len(arr) -1

    while i < j:
        arr[i],arr[j] = arr[j],arr[i]
        i += 1
        j -= 1


    return "".join(arr)

A = "abccbc"
A = 'ab'
print(solve(A))

