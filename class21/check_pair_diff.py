def solve(A,B):
    uniq = set()
    for i in range(len(A)):
        b1 = A[i] - B
        b2 = A[i] + B

        if b1 in uniq:
            return 1

        if b2 in uniq:
            return 1

        uniq.add(A[i])
    return 0

A = [5, 10, 3, 2, 50, 80]
B = 78

# A = [-10, 20]
# B = 30

print(solve(A,B))