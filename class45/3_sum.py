def pair_sum(A,low,k):
    n = len(A)
    i = low
    j = n-1

    while i < j:
        add = A[i] + A[j]
        if add == k:
            return

def solve(A):
    n = len(A)

    for