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

    stack =[]

    ngl = []

    for i in range(len(A)):
        while len(stack) != 0 and A[stack[-1]] <= A[i]:
            stack.pop()

        if len(stack) != 0:
            ngl.append(stack[-1])
        else:
            ngl.append(-1)

        stack.append(i)


    stack = []
    ngr = [0] * len(A)

    for i in range(len(A) - 1, -1, -1):
        while len(stack) != 0 and A[stack[-1]] <= A[i]:
            stack.pop()

        if len(stack) != 0:
            ngr[i] = stack[-1]
        else:
            ngr[i] = len(A)

        stack.append(i)

    max_sum =0

    for i in range(len(A)):
        max_sum += A[i] *(i - ngl[i]) *(ngr[i] - i)

    min_sum =0
    for i in range(len(A)):
        min_sum += A[i] *(i - nsl[i]) * (nsr[i] - i)



    ans = max_sum - min_sum


    return ans

A = [4, 7, 3, 8]
A = [1]
print(solve(A))