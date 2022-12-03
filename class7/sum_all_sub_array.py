def solve(A):
    n = len(A)
    total =0
    for i in range(n):
        sum =0
        for j in range(i,n):
            sum += A[j]
            total += sum
    return total

def eff_solve(A):
    n = len(A)
    total = 0
    for i in range(n):
        total += (i+1) * (n-i) * A[i]
    return total
# A = [1, 2, 3]
A = [2, 1, 3]
print(solve(A))
print(eff_solve(A))