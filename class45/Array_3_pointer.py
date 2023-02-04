def solve(A,B,C):
    p1 = 0
    p2 = 0
    p3 = 0
    ans = (1<< 31) -1
    while p1 < len(A) and p2 < len(B) and p3 < len(C):
        diff1 = abs(A[p1] - B[p2])
        diff2 = abs(B[p2] - C[p3])
        diff3 = abs(A[p1] - C[p3])

        tmp = max(max(diff1,diff2),diff3)

        if diff1 == tmp:
            if A[p1] < B[p2]:
                p1 += 1
            else:
                p2 += 1
        elif diff2 == tmp:
            if B[p2] < C[p3]:
                p2 += 1
            else:
                p3 += 1
        else:
            if C[p3] < A[p1]:
                p3 += 1
            else:
                p1 += 1
        ans = min(ans,tmp)
    return ans

A = [1, 4, 10]
B = [2, 15, 20]
C = [10, 12]
print(solve(A,B,C))

