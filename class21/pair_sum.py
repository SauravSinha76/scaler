def solve(A,B):
    unique = set()

    for i in range(len(B)):
        b = A - B[i]
        if b in unique:
            return 1
        unique.add(B[i])
    return 0

A = 8
B = [3, 5, 1, 2, 1, 2]
print(solve(A,B))