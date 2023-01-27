def gcd(A,B):
    if B == 0:
        return A
    return gcd(B,A%B)
def solve(A,B):
    n = len(A)
    max_point = 0
    for i in range(n):
        hm = {}
        count =0
        max_frq = 0
        for j in range(i+1,n):
            if A[i] == A[j] and B[i] == B[j]:
                count += 1
                continue
            x = A[i] - A[j]
            y = B[i] - B[j]

            gcd_res = gcd(x,y)
            x = x // gcd_res
            y = y // gcd_res

            key = str(x)+","+str(y)
            hm[key] = hm.get(key,1) + 1
            max_frq = max(max_frq,hm[key])
        max_point = max(max_point,max_frq + count)

    return max_point

A = [-1, 0, 1, 2, 3, 3]
B = [1, 0, 1, 2, 3, 4]
A = [3, 1, 4, 5, 7, -9, -8, 6]
B = [4, -8, -3, -2, -1, 5, 7, -4]
A = [ 3, -9, -3, 2, -8, 3, -4, -10, 5 ]
B = [ -7, -7, 2, -7, 2, 8, -5, -6, 6 ]
# A = [ 48, 45, -3, 7, -25, 38, 2, 13, 13, 18, -44, 34, -27, -46, 48, -39, -41, -32, -16, 17, -6, 44, -28, -44, -6, -43, -16, 30, -3, -27, 32, 38, -26, 20, 4, -44, -37 ]
# B = [ 47, -42, 41, 22, -4, -35, -45, -22, 5, -20, 21, -13, 47, 32, -48, 47, 17, -23, 30, -30, 37, 42, 44, 23, 1, -40, -9, 34, -34, 49, 16, -35, 2, -19, 31, 23, -37 ]

print(solve(A,B))
