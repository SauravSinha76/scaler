MOD = (10**9 + 7)
def solve(A):
    n = len(A)
    seat =[]
    for i in range(n):
        if A[i] == 'x':
           seat.append(i)

    mid = len(seat) // 2

    l = mid -1
    r = mid + 1
    k = 1
    res =0

    while l > -1:
        res = (res + seat[mid] - k - seat[l]) % MOD
        l -= 1
        k += 1

    k = 1
    while r < len(seat):
        res = (res + seat[r] - seat[mid] - k) %MOD
        r += 1
        k += 1


    return res % MOD

A = "....x..xx...x.."
print(solve(A))
