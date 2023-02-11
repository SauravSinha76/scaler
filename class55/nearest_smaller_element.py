def solve(A):

    stack=[]

    ans =[]

    for i in range(len(A)):
        while len(stack) != 0 and stack[-1] >= A[i]:
            stack.pop()

        if len(stack) != 0:
            ans.append(stack[-1])
        else:
            ans.append(-1)

        stack.append(A[i])

    return ans

A = [4, 5, 2, 10, 8]
A = [3, 2, 1]
print(solve(A))
