def solve(A,B):
    if (A >> B) & 1:
        return 1
    else:
        return 0


A = 5
B = 2
print(solve(A,B))