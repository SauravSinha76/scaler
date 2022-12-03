def solve(A):
    n = len(A)
    if n == 1:
        num = int(A[-1])
    elif n == 2:
        num = 10*int(A[-2]) + int(A[-1])
    else:
        num = 100*int(A[-3]) +10*int(A[-2]) + int(A[-1])

    if num % 8 == 0:
        return 1
    else:
        return 0


A = "4758310052942341036336679074241759053154797537802772"
print(solve(A))