def solve(A,n,k,tmp,ans):
    if k == 0:
        ans.append(list(tmp))
        return

    for i in range(n,A+1):
        tmp.append(i)
        solve(A,i+1,k-1,tmp,ans)

        tmp.pop()


ans =[]
tmp =[]
solve(4,1,2,tmp,ans)
print(ans)