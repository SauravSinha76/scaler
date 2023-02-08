from class54.Stack import Stack

def evaluate(first,second,op):
    if op == "+":
        return first + second
    elif op == "-":
        return first - second
    elif op == "*":
        return first * second
    else:
        return first // second

def solve(A):

    stack = Stack()
    symbol = ["+","-","*","/"]

    for a in A:
        if a in symbol:
            second = stack.top_ele()
            stack.pop()
            first = stack.top_ele()
            stack.pop()
            stack.push(evaluate(first,second,a))
        else:
            stack.push(int(a))
    return stack.top_ele()

A =   ["2", "1", "+", "3", "*"]
A = ["4", "13", "5", "/", "+"]
print(solve(A))



