def solve(A):
    return " ".join(A.split()[::-1])

def solve_2(A):
    words = A.split()
    ans = ""
    for i in range(len(words)-1,-1,-1):
        if i != len(words)-1:
            ans += " "
        ans += words[i]
    return ans
A = "the sky is blue"
print(solve(A))
print(solve_2(A))