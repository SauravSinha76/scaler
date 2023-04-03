def solve(A,B):
    n = len(A)

    total =0
    count = 0
    for i in range(n):
        if count == 0:
            for j in range(i+1,n):
                if j < i + B and A[i] < A[j]:
                    count += 1
            total += A[i] * count
        count -= 1
    return total

A = [5,6,3,4,2,1]
B = 2
print(solve(A,B))
