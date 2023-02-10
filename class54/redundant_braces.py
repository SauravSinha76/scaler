from class54.Stack import Stack


def solve(A):

    stack = Stack()
    symbol = ["+", "-", "*", "/"]

    for a in A:
        if a == ')':
            stack.pop()
            flag = True
            while stack.top_ele() != '(':
                if stack.top_ele() in symbol:
                    flag = False
                stack.pop()
            stack.pop()
            stack.push("a")
            if flag:
                return 1
        else:
            stack.push(a)

    return 0



A = "((a+b))"
# A = "(a+(a+b))"
# A = "(a*b)+(b*(d+(a)))"
# A = "(a+((b*c)+c))"
print(solve(A))