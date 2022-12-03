def solve(A):
    res =[]
    n = len(A)
    left =[0]*n
    right =[0]*n
    left[0]=1
    right[n-1] = 1
    for i in range(1,n):
       left[i] = left[i-1] *A[i-1]
    for i in range(n-2,-1,-1):
        right[i] = right[i+1] *A[i+1]
    for i in range(n):
        res.append(left[i]*right[i])
    return res

A = [1, 2, 3, 4, 5]
# A = [5, 1, 10, 1]
print(solve(A))