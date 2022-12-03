def solve(A,B,C):
    ans =1
    for i in range(B):
        ans = (ans * A) % C
    return ans

def solve_opt(A,B,C):
    ans =1

    while B > 0:

        if B & 1:
            ans = (ans * A) % C

        B = B >> 1
        A = (A * A) % C
    return ans

# A = 2
# B = 3
# C = 3

A = 5
B = 2
C = 4
print(solve(A,B,C))
print(solve_opt(A,B,C))