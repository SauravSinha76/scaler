def solve(A):
    i =1

    while (i*(i+1)) // 2 <= A:
        i += 1

    return i-1

print(solve(20))