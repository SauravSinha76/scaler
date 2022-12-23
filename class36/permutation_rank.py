def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

def count_lesser(A,index):
    n = len(A)
    count =0
    for i in range(index+1, n):
        if A[index] > A[i]:
            count += 1
    return count

def solve(A):
    n = len(A)
    factorial = fact(n)
    rank = 1
    for i in range(n):
        factorial //= n-i
        lesser = count_lesser(A,i)
        rank += lesser*factorial
    return rank

print(solve("string"))