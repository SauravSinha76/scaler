def solve(A):

    s = A.split()

    i =0
    j = len(s) -1

    while i < j:
        s[i],s[j] = s[j],s[i]
        i += 1
        j -= 1

    return " ".join(s)

A = "the sky is blue"
print(solve(A))