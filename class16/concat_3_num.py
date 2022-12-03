def solve(A,B,C):
    first = min(min(A,B),C)
    last = max(max(A,B),C)
    mid = (A+B+C) - (first + last)
    return str(first)+str(mid)+str(last)

A = 10
B = 20
C = 30

A = 55
B = 43
C = 47
print(solve(A,B,C))