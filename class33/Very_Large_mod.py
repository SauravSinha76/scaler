import math


def factorial(n):
    res = [None] * 50000
    # Initialize result
    res[0] = 1
    res_size = 1

    # Apply simple factorial formula
    # n! = 1 * 2 * 3 * 4...*n
    x = 2
    while x <= n:
        res_size = multiply(x, res, res_size)
        x = x + 1

    print("Factorial of given number is")
    i = res_size - 1
    return res


def multiply(x, res, res_size):
    carry = 0  # Initialize carry

    # One by one multiply n with individual
    # digits of res[]
    i = 0
    while i < res_size:
        prod = res[i] * x + carry
        res[i] = prod % 10  # Store last digit of
        # 'prod' in res[]
        # make sure floor division is used
        carry = prod // 10  # Put rest in carry
        i = i + 1

    # Put carry in res and increase result size
    while (carry):
        res[res_size] = carry % 10
        # make sure floor division is used
        # to avoid floating value
        carry = carry // 10
        res_size = res_size + 1

    return res_size


def power(x, y, p):
    res = 1  # Initialize result

    # Update x if it is
    # more than or equal to p
    x = x % p

    while (y > 0):

        # If y is odd, multiply
        # x with the result
        if (y & 1):
            res = (res * x) % p

        # y must be even now
        y = y >> 1  # y = y/2
        x = (x * x) % p

    return res

def solve(A,B):
    fact =1
    MOD = 10 **9 +7
    for i in range(2,B+1):
        fact = (fact*i) % (MOD-1)
    return power(A,fact,MOD) % MOD

A = 2
B = 27
print(solve(A,B))


