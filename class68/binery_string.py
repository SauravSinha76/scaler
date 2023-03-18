def solve(A,B):
    ## Aux Array to keep track of number of flips that has to be done for ith element
    flip = [0]*len(A)
    ## lastFlip to track the flip[i-1]th element
    lastFlip = 0
    i = 0
    time = 0
    while i<len(A):
        flip[i] = flip[i] + lastFlip
        ## Only flip in these two scenarios, in rest two scenarios flipping is not required
        if (A[i]=='1' and flip[i]%2==1) or (A[i]=='0' and flip[i]%2==0) :
            flip[i] += 1
            ## Mark i+B element as -1 since these elements are out of new range and need not to be flipped
            if(i+B<len(A)):
                flip[i+B] -= 1
            elif i+B>len(A):
                return -1
            time += 1
        lastFlip = flip[i]
        i += 1
    return time

A = "00010110"
B = 3
print(solve(A,B))