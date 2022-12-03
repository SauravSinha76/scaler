def expand(A,s,e):
    n = len(A)
    while s > -1 and e < n and A[s] == A[e]:
        s -= 1
        e +=1
    return e - s -1

def solve(A):
    n = len(A)
    ans =0
    start = -1
    end = -1
    for i in range(n):
        if i != 0:
            length = expand(A,i-1,i)
            if ans < length:
                ans = length
                start = i - length // 2
                end = i + length // 2
        length = expand(A,i,i)
        if ans < length:
            ans = length
            start = i - length // 2
            end = i + length // 2 + 1
    return A[start:end]

A = "qqaaaabaaa"
print(solve(A))

