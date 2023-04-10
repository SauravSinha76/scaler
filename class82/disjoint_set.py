def solve(A, B,C):
    parent = [-1] * (A + 1)

    for i in range(1, A + 1):
        parent[i] = i

    def root(x):
        if parent[x] == x:
            return x

        r = root(parent[x])
        parent[x] = r
        return r

    def union(x, y):
        rx = root(x)
        ry = root(y)

        if rx == ry:
            return False

        parent[rx] = ry
        return True

    for i in range(len(B)):
        if not union(B[i], C[i]):
            return False
    return True

A = 3
B = [1, 2]
C = [2, 3]

# A = 2
# B = [1, 2]
# C = [2, 1]
print(solve(A,B,C))
