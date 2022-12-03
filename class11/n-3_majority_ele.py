import sys


def solve(A):
    n = len(A)
    count1 = 0
    count2 = 0
    first = sys.maxsize
    second = sys.maxsize
    for i in range(n):
        if A[i] == first:
            count1 += 1
        elif A[i] == second:
            count2 += 1
        elif count1 == 0:
            first = A[i]
            count1 += 1
        elif count2 == 0:
            second = A[i]
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1

    count1 = 0
    count2 = 0

    for i in range(n):
        if A[i] == first:
            count1 += 1
        elif A[i] == second:
            count2 += 1

        if count1 > n / 3:
            return A[i]
        elif count2 > n / 3:
            return A[i]

    return -1


A =[1,2,3,1,1]
# A = [4, 4, 2, 3, 4, 4, 2, 5, 7]
print(solve(A))
