def solve(A):
    count = 0
    for i in range(len(A)):
        while A[i] != i:
            tmp = A[A[i]]
            A[A[i]] = A[i]
            A[i] = tmp
            count += 1

    return count

def solve1( A):
    count = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] == i:
                A[j] = A[i]
                A[i] = i
                count += 1
    return count
A = [ 1, 2, 3, 4,0]
A = [2, 0, 1, 3]
A =[4,7,8,3,6,9,2,5,1,0]
print(solve(A))
print(solve1(A))