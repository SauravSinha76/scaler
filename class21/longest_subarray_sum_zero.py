def solve(A):
    hm ={0:-1}
    psum =0
    max_len =0
    for i in range(len(A)):
        psum += A[i]
        if psum not in hm:
            hm[psum] = i
        else:
            sub_len = i - hm.get(psum)
            max_len = max(max_len,sub_len)
    return max_len


A = [1, -2, 1, 2]
A = [3, 2, -1]
print(solve(A))