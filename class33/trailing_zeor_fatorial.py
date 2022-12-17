def solve(A):
    count =0
    while A >= 5:
        A //= 5
        count += A
    return count
A = 28
print(solve(A))