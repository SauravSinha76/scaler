def solve(A):
    vovel = "aeiou"
    ans = ""
    for i in range(len(A)):
        if A[i] in vovel:
            ans += '#'
        elif not 'A' <= A[i] <= 'Z':
            ans += A[i]
    ans += ans
    return ans

A="AbcaZeoB"
print(solve(A))
