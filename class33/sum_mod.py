def solve(A):
    n = len(A)
    sum =0
    for i in range(n):
        for j in range(i+1,n):
            sum += A[i]%A[j]
            sum += A[j]%A[i]
    return sum

def solve1(A):
    n = len(A)
    total =0
    freq = [0]*1000
    for i in range(n):
        freq[A[i]] += 1
    for i in range(1,1000):
        for j in range(1,1000):
            total += j%i * freq[i] * freq[j]
    return total
A =[1,2,3]
A = [17, 100, 11]
print(solve(A))
print(solve1(A))
