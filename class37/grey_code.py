def solve(n):
    if n == 1:
        return [0,1]

    p = solve(n-1)
    p_len = len(p)
    ans =[]
    for i in range(p_len):
        ans.append(p[i])
    for i in range(p_len -1, -1, -1):
        ans.append(p[i]|(1 << (n-1)))
    return ans

print(solve(3))

