def solve(A):
    row = len(A)
    col = len(A[0])
    i = 0
    ans = 0
    while i < row:
        j =0
        while j < col:
            if i != 0 and A[i][j] != 0:
                A[i][j] += A[i-1][j]
            j += 1
        arr = A[i]
        print(arr)
        n = len(arr)
        nsl =[0] * n
        stack =[]

        for k in range(n):
            while len(stack) != 0 and arr[stack[-1]] >= arr[k]:
                stack.pop()

            if len(stack) != 0:
                nsl[k] = stack[-1]
            else:
                nsl[k] = -1

            stack.append(k)
        print(nsl)
        nsr =[0] * n
        stack =[]
        for k in range(n-1,-1,-1):
            while len(stack) != 0 and arr[stack[-1]] >= arr[k]:
                stack.pop()

            if len(stack) != 0:
                nsr[k] = stack[-1]
            else:
                nsr[k] = n

            stack.append(k)
        print(nsr)

        for k in range(n):
            ans = max(ans, arr[k] *(nsr[k] - nsl[k] - 1))
        i += 1
    return ans
A = [   [0, 0, 1],
        [0, 1, 1],
        [1, 1, 1],   ]
A = [
  [0, 1, 1],
  [1, 0, 0],
  [1, 0, 0],
  [1, 0, 0],
  [1, 0, 0],
  [1, 1, 1],
  [0, 1, 0]
]
print(solve(A))