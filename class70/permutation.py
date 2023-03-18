def permutation(A,n,curr_ans,ans,visit):

    if len(curr_ans) == n:
        ans.append(list(curr_ans))
        return

    for i in range(n):
        if not visit[i]:
            visit[i] = True
            curr_ans.append(A[i])
            permutation(A,n, curr_ans,ans,visit)
            curr_ans.pop()
            visit[i] = False


def solve(A):
    n = len(A)
    ans =[]
    visit = [False] * n
    permutation(A,n,[],ans,visit)
    return ans

A = [1, 17, 8]

print(solve(A))