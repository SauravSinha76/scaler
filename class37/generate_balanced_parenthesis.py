def generate(n,open,close,s,ans):
    if open == n and close == n:
        ans.append(s)
        return

    if open < n:
        generate(n,open+1,close,s+"(",ans)
    if close < open:
        generate(n,open,close+1,s+")",ans)


n =3

ans=[]

generate(n,0,0,"",ans)

for s in ans:
    print(s)


