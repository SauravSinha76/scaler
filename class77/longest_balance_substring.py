def solve(A):
    n = len(A)
    dp = [0] * (n + 1)
    cur_max = 0
    for i in range(1, n):
        j = i - dp[i] - 1
        if (A[i] in [')', ']', '}']) and j >= 0 and ((A[j] == '(' and A[i] == ')') or
                (A[j] == '[' and A[i] == ']') or
                (A[j] == '{' and A[i] == '}')):
            dp[i + 1] = dp[i] + dp[j] + 2
        cur_max = max(cur_max, dp[i + 1])
    return cur_max

A = "[()]"
# A = "[(])"
# A = "[]]"
# A = "([[]]()}[]([[]]([[]]))["
# A = "([[]]()}["
# A= "))(}[[[[)[(({))((()]]{][[[][{]]][)[]}]])])]}}[]](]())[[}[]}){[[)[][)(]{)]))[[[]{][([["
print(solve(A))