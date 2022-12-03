def power(A,B):
    ans = 1
    for _ in range(B):
        ans *=A
    return ans

def isArmstrong(A):
    tmp = A
    sum =0
    while tmp >0:
        num = tmp %10
        sum += power(num,3)
        tmp //=10
    return sum == A



def solve(A):
    ans =[]
    for i in range(1,A):
        if isArmstrong(i):
           ans.append(i)
    return ans

print(solve(500))