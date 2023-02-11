def solve(A):

    stack =[]

    while len(A) != 0:

        temp = A[-1]
        A.pop()

        while len(stack) != 0 and temp > stack[-1]:
            x = stack[-1]
            stack.pop()
            A.append(x)

        stack.append(temp)

    while len(stack) != 0:
        A.append(stack[-1])
        stack.pop()
    return A

A = [5, 4, 3, 2, 1]
A = [5, 17, 100, 11]
print(solve(A))


