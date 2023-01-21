def solve(A,B):
    n = len(A)

    pSum =[]
    pSum.append(A[0])

    for i in range(1,n):
        pSum.append(pSum[i-1] + A[i])



    i = 0
    j = 1



    while j < n:

        if i == 0:
            if pSum[j] == B:
                return A[:j+1]
            elif pSum[j] < B:
                j += 1
            else:
                i += 1
        else:
            if pSum[j] - pSum[i-1] == B:
                return A[i:j+1]
            elif pSum[j] - pSum[i-1] < B:
                j += 1
            else:
                i += 1
    return -1

A = [1, 2, 3, 4, 5]
B = 5
A = [5, 10, 20, 100, 105]
B = 35
print(solve(A,B))

