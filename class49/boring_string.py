def solve(A):

    n = len(A)

    odd = []
    even = []

    for i in range(n):
        if ord(A[i]) % 2 == 0:
            even.append(A[i])
        else:
            odd.append(A[i])


    even.sort()
    odd.sort()

    if abs(ord(even[-1]) - ord(odd[0])) != 1:
        return 1
    if abs(ord(odd[-1]) - ord(even[0])) != 1:
        return 1

    return 0

A = "abcd"
# A = "aab"
print(solve(A))