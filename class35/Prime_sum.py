def prime(A):
    num = [True] * (A + 1)
    num[0] = False
    num[1] = False

    i = 2
    while i * i <= A:
        if num[i]:
            j = i * i
            while j <= A:
                num[j] = False
                j += i
        i += 1
    return num

def solve(A):
    prime_num = prime(A)
    for i in range(A-1,-1,-1):
        if prime_num[i] and prime_num[A - i]:
            return [A - i, i]


print(solve(10))