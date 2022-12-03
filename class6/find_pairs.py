def solve(A):
    n = len(A)
    count =0
    ans =0
    for i in range(n-1,-1,-1):
        if A[i] == 'G':
            count += 1
        elif A[i] == 'A':
            ans += count
    return ans % ((10^9)+7)

def solve1(A):
    n = len(A)
    count =0
    ans =0

    for i in range(n):
        if A[i] == 'A':
            count += 1
        elif A[i] == 'G':
            ans += count
    return ans

A = "ABCGAG"
# A = "GAB"
print(solve(A))
print(solve1(A))
