def kedans(A):
    max_so_far = -(1 << 31)
    curr_sum =0

    for i in range(len(A)):
        curr_sum += A[i]

        if max_so_far < curr_sum:
            max_so_far = curr_sum

        if curr_sum < 0:
            curr_sum = 0
    return max_so_far

# A = [2,3,-6,2,4,-3,4,1]
# print(kedans(A))
def solve(A):
    n = len(A)
    m = len(A[0])
    ans = - (1<< 31)
    for st in range(n):
        a =[0] * m
        for end in range(st,n):
            for i in range(m):
                a[i] += A[end][i]
            ans = max(ans,kedans(a))
    return ans


def solve1(A):
    n = len(A)
    m = len(A[0])
    max_sum = -(1 << 31)
    for i in range(n-1,-1,-1):
        for j in range(m-2,-1,-1):
            A[i][j] += A[i][j + 1]
            max_sum = max(max_sum,A[i][j])
    for i in range(n-2,-1,-1):
        for j in range(m-1,-1,-1):
           A[i][j] += A[i + 1][j]
           max_sum = max(max_sum, A[i][j])

    return max_sum

A = [[-5,-4, -3],
     [-1,  2,  3],
     [2,  2 , 4]]
print(solve(A))
print(solve1(A))



