import functools

def solve(A,B):
    pair =[]
    n = len(A)
    for i in range(n):
        pair.append((A[i],B[i]))

    pair.sort(key= lambda x : x[1])
    ans = 1
    lastEnd = pair[0][1]
    for i in range(1,n):
        if pair[i][0] >= lastEnd:
            ans += 1
            lastEnd = pair[i][1]
    return ans


A = [1, 5, 7, 1]
B = [7, 8, 8, 8]
print(solve(A,B))
