def solve(A):
    count =0
    for i in range(A+1):
        x = i
        while x > 0:
            r = x % 10
            x = x // 10
            if r == 1:
                count += 1
    return count

def solve1(A):
    g = 0
    count =0
    pow =1
    x = 0
    while A > 0:
        r = A % 10
        A = A // 10

        if r == 0:
            count += (r * x * pow // 10) + g
        elif r == 1:
            count += (r * x * pow // 10) + g +1
        else:
            count += pow + (r * x * pow // 10)
        g += r * pow
        pow *= 10
        x += 1
    return count


def countDigitOne(n):
    countr = 0
    i = 1
    while i <= n:
        divider = i * 10
        countr += (n // divider) * i + min(max(n % divider - i +1, 0), i)
        i *= 10

    return countr
print(solve(101))
print(solve1(101))
print(countDigitOne(101))