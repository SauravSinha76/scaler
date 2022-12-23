def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

def count_lesser(A,index):
    n = len(A)
    freq = {}
    count =0
    ans =1
    for i in range(n):
        freq[A[i]] = freq.get(A[i],0)+1
    for a in freq:
        if A[index] >= a:
            ans *= fact(freq[a])
    if ans  == 1:
        return 0
    else:
        return ans


def solve(A):
    n = len(A)
    factorial = fact(n)
    rank = 1
    for i in range(n):
        factorial //= n-i
        lesser = count_lesser(A,i)
        if lesser != 0:
            rank += factorial // lesser
    return rank


A = "bcab"
print(solve(A))