def solve(A):
    if A <= 1:
        return A

    return solve(A-1) + solve(A -2)
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
    return 0

if __name__ == '__main__':
    main()