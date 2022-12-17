def gcd(A,B):
    if B == 0:
        return A
    return gcd(B, A%B)

def sqrt(n):
    i = 1
    while i*i <= n:
        if i*i == n:
            return i
        i += 1
    return -1

def solve(A):
    n = len(A)
    # Sort array in decreasing order
    A.sort(reverse=True)

    freq = [0 for i in range(A[0] + 1)]

    # Count frequency of each element
    for i in range(n):
        freq[A[i]] += 1

    # Size of the resultant array
    size = sqrt(n)
    brr = [0 for i in range(len(A))]
    l = 0

    for i in range(n):
        if (freq[A[i]] > 0):

            # Store the highest element in
            # the resultant array
            brr[l] = A[i]

            # Decrement the frequency of that element
            freq[brr[l]] -= 1
            l += 1
            for j in range(l):
                if (i != j):
                    # Compute GCD
                    x = gcd(A[i], brr[j])

                    # Decrement GCD value by 2
                    freq[x] -= 2
    return brr[:size]


print(sqrt(16))
A = [2, 2, 2, 2, 8, 2, 2, 2, 10]
# A = [5, 5, 5, 15]
print(solve(A))
