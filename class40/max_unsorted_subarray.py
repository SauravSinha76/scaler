def solve(A):
    n = len(A)
    left = 0
    right = n-1
    while left < right:
        if A[left] <= A[left+1]:
            left += 1
        elif A[right] >= A[right-1]:
            right -= 1
        else:
            break

    max_val = A[left]
    min_val = A[left]

    for i in range(left+1,right+1):
        max_val = max(max_val,A[i])
        min_val = min(min_val,A[i])

    for i in range(left):
        if A[i] > min_val:
            left = i
            break

    for i in range(n-1,right,-1):
        if A[i] < max_val:
            right = i
            break

    if left == right:
        return [-1]
    else:
        return [left,right]



A = [1, 3, 2, 4, 5]
A = [1, 1]
# A = [ 4, 15, 4, 4, 15, 18, 20 ]
print(solve(A))
