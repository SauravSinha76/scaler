def solve(A):
    xor_res = 0
    for i in range(len(A)):
        xor_res ^= A[i]

    idx = -1
    for i in range(31):
        if xor_res & 1 << i:
            idx = i
            break

    set1 = 0
    set2 = 0
    for i in range(len(A)):
        if A[i] & 1 << idx:
            set1 ^= A[i]
        else:
            set2 ^= A[i]

    return [set1, set2]

A = [1, 2, 3, 1, 2, 4]
A = [1, 2]
print(solve(A))