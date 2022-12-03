def solve(A):
    n = len(A)
    if n < 1:
        return 0

    if A[0] == 0:
        count = 1
    else:
        count = 0

    for i in range(1,n):
        if A[i] != A[i-1]:
            count += 1
    return count

def solve1(A):
    n = len(A)
    if n < 1:
        return 0

    count =0

    for i in range(n):
        if (count % 2 == 0 and A[i] == 0) or (count % 2 == 1 and A[i] == 1):
            count += 1
    return count


A = [1,0, 1, 0]
print(solve(A))
print(solve1(A))
