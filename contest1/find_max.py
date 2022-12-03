def solve(A,B):
    n = len(A)

    count = 0
    exists = False

    for i in range(n):
        if A[i] > B:
            count += 1
        elif A[i] == B:
            exists = True

    if exists:
        return count
    else:
        return -1


A = [2,4,1]
B = 3
print(solve(A,B))