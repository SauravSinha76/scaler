def solve(A):
    n = len(A)
    count =0
    ans =0
    vovels = 'AEIOU'
    A = A.upper()
    for i in range(n-1,-1,-1):
        count +=1
        if A[i] in vovels:
            ans += count
    return ans
A ='BDCF'
print(solve(A))

