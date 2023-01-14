def search(A, B):
    n = len(A)
    m = len(A[0])
    i = 0

    # set indexes for top right element
    j = m - 1
    while i < n and j >= 0:

        if A[i][j] == B:
            return 1
        elif A[i][j] > B:
            j -= 1
        else:
            i += 1
    return 0

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

A = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50],
    ]
B = 3

A = [
      [5, 17, 100, 111],
      [119, 120, 127, 131],
    ]
B = 3
print(search(A,B))