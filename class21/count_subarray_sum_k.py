def solve(A,B):
    count = 0
    psum =0
    prevSum= {}
    for i in range(len(A)):
        psum += A[i]

        if psum == B:
            count +=1

        if (psum - B) in prevSum:
            count += prevSum[psum - B]

        if psum in prevSum:
            prevSum[psum] += 1
        else:
            prevSum[psum] = 1

    return count

A = [1, 0, 1]
B = 1
print(solve(A,B))