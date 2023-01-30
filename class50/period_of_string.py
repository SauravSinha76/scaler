def solve(A):
    n = len(A)
    Z = []
    L = 0
    R = 0
    Z.append(0)
    for i in range(1, n):
        if i > R:
            j =i
            k =0

            while j < n and A[j] == A[k]:
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
                while j < n and A[j] == A[k]:
                    j += 1
                    k += 1
                Z.append(k)
                L = i
                R = j - 1
    return Z

def solve_lps(A):
    n = len(A)
    lps =[0] * n

    l = 0

    i =1
    while i < n:

        if A[l] == A[i]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l != 0:
                l= lps[l-1]
            else:
                lps[i] = 0
                i += 1
    return lps
def solve(A):

    lps = solve_lps(A)
    return len(A) - lps[-1]
A = "abababab"
A = "AAACAAAAAAAAAAAACAAAA"
print(solve(A))
print(solve_lps(A))

