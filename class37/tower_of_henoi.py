def toh(n,source,destination,auxillari,ans):
    if n == 0:
        return
    toh(n-1,source,auxillari,destination,ans)
    ans.append([n,source,destination])
    toh(n-1,auxillari,destination,source,ans)

A = 6
ans =[]
toh(A,1,3,2,ans)
print(len(ans))
print(ans)