def solve(A):

    n = len(A)
    ans = [0]*n
    stack =[]
    for i in range(n-1,-1,-1):
        while len(stack) != 0 and stack[-1] <= A[i]:
            stack.pop()

        if len(stack) != 0:
            ans[i] = stack[-1]
        else:
            ans[i] = -1

        stack.append(A[i])
    return ans
A = [4, 5, 2, 10]
A = [3, 2, 1]
A = [ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]
print(solve(A))
