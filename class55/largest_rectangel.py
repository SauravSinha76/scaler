def solve(A):
    stack = []

    nsl = []

    for i in range(len(A)):
        while len(stack) != 0 and A[stack[-1]] >= A[i]:
            stack.pop()

        if len(stack) != 0:
            nsl.append(stack[-1])
        else:
            nsl.append(-1)

        stack.append(i)

    print(nsl)
    stack =[]
    nsr =[0] *len(A)

    for i in range(len(A)-1,-1,-1):
        while len(stack) != 0 and A[stack[-1]] >= A[i]:
            stack.pop()

        if len(stack) != 0:
            nsr[i]=stack[-1]
        else:
            nsr[i]=len(A)

        stack.append(i)

    print(nsr)
    ans = 0

    for i in range(len(A)):
        ans = max(ans,A[i]*(nsr[i] - nsl[i] -1))

    return ans

A = [2, 1, 5, 6, 2, 3]
print(solve(A))