from class54.Stack import Stack


def solve(A):

    stack = Stack()
    hm = {
        ')' : '(',
        '}' : '{',
        ']' : '['

    }
    for a in A:
        if a not in hm:
            stack.push(a)
        else:
            if stack.size == 0:
                return False
            if stack.top_ele() != hm[a]:
                return False
            else:
                stack.pop()

    if stack.size == 0:
        return True
    else:
        return False


A = "{([])}"
A = "(){"
A = "()[]"
print(solve(A))

