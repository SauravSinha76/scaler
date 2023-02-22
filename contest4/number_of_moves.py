def solve(A):
    left =0
    right = len(A)-1

    gap= []
    j =0
    for i in range(A[-1]):
        if i != A[j]:
            gap.append(i)
    while len(gap):
        gap.pop()
