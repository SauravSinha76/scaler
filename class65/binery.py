def solve(A):
    ans =""
    for i in range(31,-1,-1):
        if A >> i & 1:
            ans += '1'
        else:
            ans += '0'
    return ans
print(solve(31))