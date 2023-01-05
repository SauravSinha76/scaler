def merge(A,B):
    m = len(A)
    n = len(B)
    i = 0
    j = 0
    C = []
    while i < m and j < n:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[i])
            j += 1
    while i < m:
        C.append(A[i])
        i += 1
    while j < n:
        C.append(B[j])
        j += 1
    return C


