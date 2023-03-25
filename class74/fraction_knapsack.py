import functools

def compair(x,y):
    x_ratio = x(0) /x(1)
    y_ratio = y(0) / y(1)

    if x_ratio > y_ratio:
        return 1
    else:
        return 0

def solve(A,B,C):
    n = len(A)
    D =[]

    for i in range(n):
        D.append((A[i],B[i]))

    D.sort(key= lambda x : x[0]/x[1],reverse=True)
    print(D)
    ans = 0
    for i in range(n):
        if C >0:
            if C > D[i][1]:
                ans += D[i][0]
                C -= D[i][1]
            else:
                ratio = D[i][0]/D[i][1]
                ans += C * ratio
                C = 0
    return int(ans * 100)
A = [60, 100, 120]
B = [10, 20, 30]
C = 50
A = [10, 20, 30, 40]
B = [12, 13, 15, 19]
C = 10
print(solve(A,B,C))