def solve(A,B):
    C = B +"$"+A
    n = len(C)
    Z = []
    L = 0
    R = 0

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

def solvr_brute(A,B):
    C = B+"$"+A

    n = len(C)

    Z = []

    for i in range(1,n):
        k = 0
        j = i
        while j < n and C[j] == C[k]:
            k += 1
            j += 1
        Z.append(k)
    return Z

A = "mynameissaurav"
B ="meis"
print(solve(A,B))
print(solvr_brute(A,B))