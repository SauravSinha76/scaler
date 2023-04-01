
def solve(A):
    n = len(A)
    max_length = 0
    open = 0
    close =0
    for j in range(n):
        if A[j] == '(':
            open +=1
        else:
            close += 1
        if open == close:
            max_length = max(max_length,open + close)
        elif open < close:
            open = 0
            close = 0

    open = 0
    close = 0
    for j in range(n-1,-1,-1):
        if A[j] == '(':
            open += 1
        else:
            close += 1
        if open == close:
            max_length = max(max_length, open + close)
        elif open > close:
            open = 0
            close = 0
    return max_length
A = ')()())'
print(solve(A))



