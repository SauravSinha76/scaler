


def reverse(A,i,j):
    while i<j:
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
        i += 1
        j -= 1

def solve(A,B):
    n = len(A)
    res =[]
    for b in B:
        tmp = list(A)
        reverse(tmp,0,n-1)
        reverse(tmp,0,n-b-1)
        reverse(tmp,n-b,n-1)
        res.append(tmp)

    return res

A = [1, 2, 3, 4, 5]
B = [2, 3]
print(solve(A,B))


