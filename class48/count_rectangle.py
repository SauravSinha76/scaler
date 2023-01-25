def solve(A,B):
    n = len(A)

    coordinate = set()

    for i in range(n):
        coordinate.add(str(A[i])+","+str(B[i]))
    count =0
    for i in range(n):
        for j in range(i+1, n):
            if A[i] != A[j] and B[i] != B[j]:
                if str(A[i])+","+str(B[j]) in coordinate and str(A[j])+","+str(B[i]) in coordinate:
                    count += 1
    return count

A = [1, 1, 2, 2]
B = [1, 2, 1, 2]
# A = [1, 1, 2, 2, 3, 3]
# B = [1, 2, 1, 2, 1, 2]
print(solve(A,B))
