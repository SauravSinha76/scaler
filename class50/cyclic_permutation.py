def reverse(A, i, j):
    while i < j:
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
        i += 1
        j -= 1


def rotate(A, n):
    reverse(A, 0, n - 1)
    reverse(A, 0, 0)
    reverse(A, 1, n - 1)


def solve(A, B):
    A = list(A)
    B = list(B)
    n = len(A)
    count = 0
    for i in range(n):
        rotate(A, n)
        print(A)
        if A == B:
            count += 1
    return count


def solve_op(A, B):
    b = 2
    hash_A = 0
    n = len(A)
    power = 1
    for i in range(n - 1, -1, -1):
        hash_A += int(A[i]) * power
        power *= b

    hash_B = 0
    m = len(B)
    power = 1
    for i in range(m - 1, -1, -1):
        hash_B += int(B[i]) * power
        power *= b

    print(hash_A)
    print(hash_B)
    power //= b
    count = 0
    for i in range(m):
        hash_B = (hash_B - int(B[i]) * power) * b + int(B[i])
        print("hash")
        print(hash_B)
        if hash_B == hash_A:
            count += 1
    return count


A = "1001"
B = "0011"
# A = "111"
# B = "111"
A = "0011000010"
B = "0101000001"
print(solve(A, B))
print(solve_op(A, B))
