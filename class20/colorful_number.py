def solve(A):
    pow = 10
    unique = set()
    while A > 0:
        n = A
        p =1
        while n > 0:
            p *= n % pow
            n //= pow
            if p in unique:
                return 0
            unique.add(p)
        A //= pow
    return 1

print(solve(2345))