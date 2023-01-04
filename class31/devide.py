def solve(A, B):
    sign = -1 if (A < 0) ^ (B < 0) else 1

    # remove sign of operands
    dividend = abs(A)
    divisor = abs(B)

    # Initialize
    # the quotient
    quotient = 0
    temp = 0

    # test down from the highest
    # bit and accumulate the
    # tentative value for valid bit
    for i in range(31, -1, -1):
        if temp + (divisor << i) <= dividend:
            temp += divisor << i
            quotient |= 1 << i
    # if the sign value computed earlier is -1 then negate the value of quotient
    quotient *= sign
    if quotient > (1 << 31) -1:
        return (1 << 31) -1
    return quotient

def divide( A, B):
    sign = -1 if (A < 0) ^ (B < 0) else 1

    dividend = abs(A)
    divisor = abs(B)

    qua = 0
    temp = 0

    for i in range(31, -1, -1):
        if temp + (divisor << i) <= dividend:
            temp += divisor << i
            qua |= 1 << i

    qua *= sign

    if qua > (1 << 31) - 1:
        return (1 << 31) - 1
    return qua

print(1 << 31 -1)
A = 2147483647
B = 1
print(solve(A,B))
print(divide(A,B))