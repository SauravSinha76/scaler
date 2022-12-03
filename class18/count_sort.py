import sys


def solve(A):
    max_val = max(A)
    max_val +=1
    count =[0]*max_val

    for i in A:
        count[i] += 1

    k =0
    for i in range(max_val):
        for j in range(count[i]):
            A[k] = i
            k += 1
    return A

A = [1, 3, 1]
print(solve(A))