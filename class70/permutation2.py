def permutation(A,n,r,curr_ans,ans,freq):

    if len(curr_ans) == n:
        ans.append(list(curr_ans))
        return

    for i in range(r):
        if freq[i] > 0:
            freq[i] -= 1
            curr_ans.append(i)
            permutation(A,n,r, curr_ans,ans,freq)
            curr_ans.pop()
            freq[i] += 1


def solve(A):
    n = len(A)
    ans =[]
    freq = [0] * 11
    for i in range(n):
        freq[A[i]] += 1
    permutation(A,n,11,[],ans,freq)
    return ans

A = [1,1, 2]

print(solve(A))