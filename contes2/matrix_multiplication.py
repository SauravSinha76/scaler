def solve(A,B):
    n1 = len(A)
    m1 = len(A[0])

    n2 = len(B)
    m2 = len(B[0])

    res = [[0 for columns in range(m2)]
           for rows in range(n1)]
    if m1 != n2:
        print("Multiplication is not possible")
        return

    else:
        for i in range(n1):
            for j in range(m2):
                for k in range(m1):
                    res[i][j] += A[i][k] * B[k][j]

    return res


A = [
        [1,2,3],
        [4,5,6]
    ]

B = [
        [7, 8],
        [9, 10],
        [11,12]
    ]

print(solve(A,B))
