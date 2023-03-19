def solve(A):
    n = len(A)
    max_pro = - 1<< 31
    for i in range(n):
        for j in range(i+1,n):
            pro = 1
            for k in range(i,j):
                pro *= A[k]

            max_pro = max(max_pro,pro)

    return max_pro

def solve1(A):
    n = len(A)
    max_pro = A[0]
    min_pro = A[0]
    ans = A[0]
    for i in range(1,n):

        if A[i] < 0:
            max_pro, min_pro = min_pro, max_pro

        min_pro = min(A[i], A[i]* min_pro)
        max_pro = max(A[i], A[i]* max_pro)

        ans = max(ans,max_pro,min_pro)

    return ans

A = [4, 2, -5, 1]
A = [0,0,0,0,3,3,0,0]
print(solve(A))
print(solve1(A))
