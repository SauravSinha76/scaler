
def subset(A,n,idx,sub,ans):
    if idx == n:
        ans.append(list(sub))
        return
    for j in range(idx, n):
        if j == idx or A[j] != A[j-1]:
            sub.append(A[j])
            subset(A,n,j+1,sub,ans)
            sub.pop()



def solve(A):
    ans=[]
    A.sort()
    subset(A,len(A),0,[],ans)
    return ans

A = [1, 1, 3]
# A = [ 9, -20, -11, -8, -4, 2, -12, 14, 1, -18 ]
print(solve(A))