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

def duplicate(A,index):
    n = len(A)
    freq = {}
    ans =1
    for i in range(index,n):
        freq[A[i]] = freq.get(A[i],0)+1
    for a in freq:
            ans *= fact(freq[a])
    return ans


def solve(A):
    n = len(A)
    factorial = fact(n)
    rank = 1
    for i in range(n):
        factorial //= n-i
        lesser = count_lesser(A,i)
        den = duplicate(A,i)
        rank += factorial * lesser // den
    return rank


A = "bcab"
print(solve(A))