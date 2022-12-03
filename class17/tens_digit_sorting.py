import functools


def get_tens_digit(x):
    x = x // 10
    x = x % 10
    return x


def comparator(x, y):
    x_tens = get_tens_digit(x)
    y_tens = get_tens_digit(y)

    if x_tens < y_tens:
        return -1
    elif x_tens == y_tens and x > y:
        return -1
    return 1


def solve(A):
    A.sort(key=functools.cmp_to_key(comparator))
    return A

A = [15, 11, 7, 19]
A = [2, 24, 22, 19]
print(solve(A))
print(get_tens_digit(329))