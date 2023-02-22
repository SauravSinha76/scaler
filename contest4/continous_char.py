def solve(A,B,C):

    n = len(A)
    max_count =0

    for i in range(n):
        count = 0
        k = 0
        for j in range(i,n):
            if A[j] == C:
                count += 1
            elif k < B:
                count += 1
                k += 1
            else:
                break
        max_count = max(max_count,count)
    return max_count

A ="oyoroom"
B = 1
C = "o"

A = "abacus"
B = 2
C = "a"
print(solve(A,B,C))