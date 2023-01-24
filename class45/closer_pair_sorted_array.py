def solve(A,B,C):
    n = len(A)
    m = len(B)

    ans =[n,m]
    min_diff = (1 << 31) -1
    i =0
    j = m-1

    while i < n and j > -1:
        p = A[i] + B[j]
        diff = abs(C -p)
        if min_diff > diff:
            ans[0] = i
            ans[1] = j
            min_diff = diff
        elif min_diff == diff and ans[0] >= i and ans[1] >= j:
            ans[0] = i
            ans[1] = j


        if p > C:
            j -= 1
        else:
            i += 1
    return [A[ans[0]],B[ans[1]]]


A = [1, 2, 3, 4, 5]
B = [2, 4, 6, 8]
C = 9

A = [5, 10, 20]
B = [1, 2, 30]
C = 13

A = [ 1 ]
B = [ 2, 4 ]
C = 4
print(solve(A,B,C))