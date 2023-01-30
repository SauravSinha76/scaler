def check_pelindrome(A):
    n = len(A)
    i =0
    j = n-1
    while i < j:
        if A[i] != A[j]:
            return False
        i += 1
        j -= 1
    return True
def solve(A):
    n = len(A)
    for i in range(n,0,-1):
        if check_pelindrome(A[:i]):
            return n - i
    return n-1

def solve(A):
    n = len(A)

    low = 0
    high = n-1

    while low <= high:
        mid = (low + high)//2

        if check_pelindrome(A[:mid+1]):
            low = mid + 1
        else:
            high = mid - 1
    return n - low


def computeLPSArray(string):

    M = len(string)
    lps = [0] * M

    length = 0
    lps[0] = 0  # lps[0] is always 0

    # the loop calculates lps[i]
    # for i = 1 to M-1
    i = 1
    while i < M:

        if string[i] == string[length]:

            length += 1
            lps[i] = length
            i += 1

        else:  # (str[i] != str[len])

            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is
            # similar to search step.
            if length != 0:

                length = lps[length - 1]

                # Also, note that we do not
                # increment i here

            else:  # if (len == 0)

                lps[i] = 0
                i += 1

    return lps
def solve_lps(A):
    string = A+"$"+A[::-1]
    lps = computeLPSArray(string)
    return len(A) - lps[-1]

def z_algo(A):
    C = A +"$"+A[::-1]
    n = len(C)
    Z = []
    L = 0
    R = 0
    Z.append(0)
    for i in range(1, n):
        if i > R:
            j =i
            k =0

            while j < n and C[j] == C[k]:
                j += 1
                k += 1
            Z.append(k)
            L =i
            R = j -1
        else:
            if Z[i -L] < R -i + 1:
                Z.append(Z[i-L])
            else:
                j = R+1
                k = R - i +1
                while j < n and C[j] == C[k]:
                    j += 1
                    k += 1
                Z.append(k)
                L = i
                R = j - 1
    return Z
A = "aaaa"
# A = "mmtatbdzqsoemuvnpppsu"
print(solve(A))
print(computeLPSArray(A+"$"+A[::-1]))
print(z_algo(A))
print(solve_lps(A))