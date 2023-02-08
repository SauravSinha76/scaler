from class54.Stack import Stack


def solve(A,B,C):

    stack = Stack()

    stack.push(B)

    for c in C:
        if c == 0:
            stack.pop()
        else:
            stack.push(c)

    return stack.top_ele()

A = 10
B = 23
C = [86, 63, 60, 0, 47, 0, 99, 9, 0, 0]

A = 1
B = 1
C = [2]
print(solve(A,B,C))