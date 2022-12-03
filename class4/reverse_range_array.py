def solve(A, B, C):
    while B < C:
        A[B], A[C] = A[C], A[B]
        B += 1
        C -= 1
    return A


# A = [1, 2, 3, 4]
# B = 2
# C = 3
if __name__ == "__main__":
    A = [2, 5, 6]
    B = 0
    C = 2
    print(solve(A, B, C))
