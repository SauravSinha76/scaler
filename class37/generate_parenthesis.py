def solve(n,open,close,paran,ans):
    if open == n and close == n:
        ans.append(paran)
        return

    if open < n:
        solve(n,open+1,close,paran+"(",ans)
    if close < open:
        solve(n,open,close+1,paran+")",ans)


ans = []
n = 3
solve(n,0,0,"",ans)
print(len(ans))
print(ans)