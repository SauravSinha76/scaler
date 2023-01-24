def solve(A,B):
    A.sort()
    C =[]

    hm ={}
    for i in range(len(A)):
        hm[A[i]]=hm.get(A[i],0)+ 1

    for i in range(len(B)):
        if B[i] in A:
            C.append(B[i])
            j =1
            while j<hm[B[i]]:
                C.append(B[i])
                j += 1


    for i in range(len(A)):
        if A[i] not in B:
            C.append(A[i])

    return C

A = [1, 2, 3, 4, 5]
B = [5, 4, 2]
A = [ 3, 20, 17, 17 ]
B = [ 5, 9, 20, 11, 6, 18, 7, 13 ]
A = [ 10, 2, 18, 16, 16, 16 ]
B = [ 3, 13, 2, 16, 4, 19 ]
print(solve(A,B))

