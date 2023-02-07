def solve(A):
    A.append(0)

    n = len(A)

    area = 0

    for i in range(n):
        if i == 0:
            area += A[i]/2
        else:
            area += abs(A[i] - A[i-1])/2 + min(A[i],A[i-1])

    return int(area)

def solve1(A):
    return sum(A)
A=[2,1,3]
print(solve(A))
print(solve1(A))