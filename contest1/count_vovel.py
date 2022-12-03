def solve(A,B):
    psum = [0] * len(A)
    vovel ="aeiou"
    for i in range(len(A)):
        if A[i] in vovel:
            psum[i] += 1

        if i != 0:
            psum[i] += psum[i-1]


    ans = []
    for i in range(len(B)):
        l = B[i][0]
        r = B[i][1]

        if l == 0:
            ans.append(psum[r])
        else:
            ans.append(psum[r] - psum[l-1])

    return ans


A = "scaler"
B = [[0,2],
     [2,4]]

A = "interviewbit"
B = [[0,4],
     [9,10]]
print(solve(A,B))