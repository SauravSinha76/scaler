def solve(A,B):
    arr = []
    n = len(A)
    for i in range(n):
        if A[i] == '0':
            arr.append(0)
        else:
            arr.append(1)
    ans = 0
    for i in range(n-B+1):
        if arr[i] == 0:
            for j in range(i,B+i):
                arr[j] = arr[j] ^ 1

            ans += 1

    for i in range(n):
        if arr[i] == 0:
            return -1

    return ans

A = "00010110"
B = 3
A = "011"
B = 3
print(solve(A,B))