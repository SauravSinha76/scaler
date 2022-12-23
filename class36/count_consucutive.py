
def countConsecutive(N):
    # constraint on values of L gives us the
    # time Complexity as O(N ^ 0.5)
    count = 0
    L = 0
    a = 1
    while a > 0:
        a = (N / (L+1)) - L / 2
        if a > 0 and a - int(a) == 0.0:
            print(f"{L}:{a}")
            count += 1
        L += 1
    return count

def consecutiveNumbersSum( N: int) -> int:
    if N == 1:
        return 1
    res = 1
    i = 2
    while i * i < N+1:
        if N % i == 0:
            if i % 2 == 1:  # If i is odd, then we can form a sum of length i
                res += 1
            j = (N // i)  # Check the corresponding N // i
            if i != j and j % 2 == 1:
                res += 1
        i += 1
    if N % 2 == 1:  # If N is odd(2k + 1). Then N = k + k + 1, not included above
        res += 1

    return res

print(countConsecutive(15))
print(consecutiveNumbersSum(15))