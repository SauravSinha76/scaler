def solve(A,B):

    n = len(A)
    l = 0
    count_0= 0
    left = -1
    right = -1
    max_length = 0
    for i in range(n):
        if A[i] == 0:
            count_0 += 1
        if count_0 > B:
            if A[l] == 0:
                count_0 -= 1
            l += 1
        if max_length < (i - l +1):
            max_length = i - l +1
            left = l
            right = i
    ans= []
    for i in range(left, right+1):
        ans.append(i)
    return ans

A = [1,1,0,1,1,0,0,1,1,1]
B = 1
A = [1, 0, 0, 0, 1, 0, 1]
B = 2
print(solve(A,B))