def solve(A):
    if A == 0 or A == 1:
        return 1

    return solve(A-1) + (A-1) * solve(A-2)

def memo_solve(A):

    dp_0 = 1
    dp_1 = 1
    ans = dp_1
    for i in range(2 , A+1):
        ans = dp_1 + ((i-1) * dp_0)
        dp_0 = dp_1
        dp_1 = ans
    return ans % 10003

print(solve(4))
print(memo_solve(4))