def solve(A):
    if A <= 1:
        return A

    return solve(A-1) + solve(A -2)
def solve_memo(A, dp):
    if A <= 1:
        return A

    if dp[A] != -1:
        return dp[A]

    dp[A] = solve_memo(A-1,dp) + solve_memo(A-2,dp)
    return dp[A]
def teb_solve(A):
    if A <= 1:
        return 1

    dp_1 = 0
    dp_2 = 1

    ans = dp_2

    for i in range(2, A+1):
        ans = dp_2 + dp_1
        dp_1 = dp_2
        dp_2 = ans
    return ans
def main():
    A = int(input())
    print(teb_solve(A))
    dp =[-1 for _ in range(A+1)]
    print(solve_memo(A,dp))
    return 0

if __name__ == '__main__':
    main()