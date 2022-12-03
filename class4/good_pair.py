def solve(A,B):
    n = len(A)
    for i in range(n):
        for j in range(i+1,n):
            if A[i]+A[j] == B:
                return 1
    return 0


A =[1,2,2]
B=4
print(solve(A,B))