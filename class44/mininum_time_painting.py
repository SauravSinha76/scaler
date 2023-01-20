def count_painter(A,time):
    count = 1
    timeLeft = time

    for i in range(len(A)):
        if A[i] <= timeLeft:
            timeLeft -= A[i]
        else:
            count += 1
            timeLeft = time- A[i]
    return count

def solve(A,B,C):
    r = sum(C)
    l = max(C)
    ans = 0
    while l <= r:
        mid = (l+r)//2

        p = count_painter(C,mid)

        if p <= A:
            ans = mid
            r = mid -1
        else:
            l = mid + 1
    return ans *B

A = 2
B = 5
C = [1, 10]

# A = 10
# B = 1
# C = [1, 8, 11, 3]
A = 3
B = 10
C = [ 185, 186, 938, 558, 655, 461, 441, 234, 902, 681 ]
print(solve(A,B,C))
print(count_painter(C,1867))