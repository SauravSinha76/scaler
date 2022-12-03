def solve(A):
    n = len(A)
    count =0
    if n < 2:
        return count
    peven = [0] * n
    podd = [0] * n

    peven[0] = A[0]
    podd[1] = A[1]

    for i in range(1, n):
        if i % 2 == 0:
            peven[i] = A[i] +peven[i - 1]
            podd[i] = podd[i - 1]
        else:
            peven[i] = peven[i-1]
            podd[i] = A[i] + podd[i - 1]


    for i in range(n):

        sum_even = podd[n - 1] - podd[i]
        if i != 0:
            sum_even += peven[i - 1]

        sum_odd = peven[n - 1] - peven[i]
        if i != 0:
            sum_odd += podd[i - 1]

        if sum_odd == sum_even:
            count += 1
    return count

A=[2, 1, 6, 4]
# A=[1, 1, 1]
print(solve(A))