import sys


def solve(A):
    n = len(A)
    feq =0
    maj_ele =sys.maxsize
    for i in range(0,n):
        if maj_ele == A[i]:
            feq +=1
        elif feq == 0:
            maj_ele = A[i]
            feq += 1
        else:
            feq -= 1

    if feq > 0:
        return maj_ele
    else:
        count =0
        for i in range(n):
            if maj_ele == A[i]:
                count += 1

        if count > n/2:
            return maj_ele

A = [2, 1, 2]
print(solve(A))
