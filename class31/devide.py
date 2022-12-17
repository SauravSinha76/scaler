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


A = -2147483648
B = -1
print(solve(A,B))