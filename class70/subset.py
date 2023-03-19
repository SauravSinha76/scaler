
def subset(A,n,idx,sub,ans):
    if idx == n:
        ans.append(list(sub))
        return

    subset(A, n, idx + 1, sub, ans)
    sub.append(A[idx])
    subset(A,n,idx+1,sub,ans)
    sub.pop()



def solve(A):
    ans=[]
    A.sort()
    subset(A,len(A),0,[],ans)
    return ans

A = [1, 2, 3]
A = [ 9, -20, -11, -8, -4, 2, -12, 14, 1, -18 ]
print(solve(A))