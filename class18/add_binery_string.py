def solve(A,B):
    n = max(len(A),len(B))
    A = A.zfill(n)[::-1]
    B = B.zfill(n)[::-1]
    ans = ""
    i = 0
    carry =0
    while i < n:
        x = int(A[i]) + int(B[i]) + carry

        if x == 0:
            ans += '0'
            carry = 0
        elif x == 1:
            ans += '1'
            carry = 0
        elif x == 2:
            ans += '0'
            carry = 1
        elif x == 3:
            ans += '1'
            carry = 1
        i += 1

    if carry == 1:
        ans += '1'

    return ans[::-1]

a = "1010110111001101101000"

b = "1000011011000000111100110"
print(solve(a,b))
