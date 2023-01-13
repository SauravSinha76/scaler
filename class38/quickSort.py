def rearrange(A,s,e):
    p1 = s+1
    p2 = e

    while p1 <= p2:
        if A[p1] <= A[s]:
            p1 += 1
        elif A[p2] > A[s]:
            p2 -= 1
        else:
            A[p1],A[p2] = A[p2],A[p1]
            p1 += 1
            p2 -= 1
    A[s],A[p2] = A[p2],A[s]
    return p2

def sort(A,s,e):
    if s >= e : return

    p = rearrange(A,s,e)
    sort(A,s,p-1)
    sort(A,p+1,e)


def solve(A):
    sort(A,0,len(A)-1)

A = [9,8,7,6,5,4,3,2,1]
solve(A)
print(A)