def solve(A,B):
    n = len(A)

    k=0

    for i in range(n):
        if A[i] <= B:
            k += 1

    if k <= 1:
        return 0

    swap =0
    for i in range(k):
        if A[i] > B:
            swap +=1

    min_swap = swap

    start =1
    end = k

    while end < n:
        if A[start-1] > B:
            swap -= 1
        if A[end] > B:
            swap += 1
        if swap < min_swap:
            min_swap = swap
        start +=1
        end +=1

    return min_swap

# A = [1, 12, 10, 3, 14, 10, 5]
# B = 8

A = [5, 17, 100, 11]
B = 20
print(solve(A,B))