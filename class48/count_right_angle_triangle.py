def solve(A,B):
    n = len(A)
    count =0
    for i in range(n):
        for j in range(n):
            if i != j:
                for k in range(n):
                    if i != j and i != k:
                        if A[i] == A[j] and B[i] == B[k]:
                            count += 1
    return count

def solve1(A,B):
    n = len(A)
    count =0
    coordinate = set()
    for i in range(n):
        coordinate.add(str(A[i])+","+str(B[i]))
    for i in range(n):
        for j in range(i+1,n):
            if A[i] != A[j] and B[i] != B[j]:
                if str(A[i])+","+str(B[j]) in coordinate:
                    count += 1
                if str(A[j])+","+str(B[i]) in coordinate:
                    count += 1
    return count

def solve2(A,B):
    hm_A = {}
    hm_B = {}
    n = len(A)
    count = 0
    for i in range(n):
        hm_A[A[i]] = hm_A.get(A[i],0) + 1
        hm_B[B[i]] = hm_B.get(B[i],0) + 1

    for i in range(n):
        c1 = hm_A[A[i]] -1
        c2 = hm_B[B[i]] -1
        count += c1 * c2
    return count


A = [1, 1, 2]
B = [1, 2, 1]
A = [1, 1, 2, 3, 3]
B = [1, 2, 1, 2, 1]
print(solve(A,B))
print(solve1(A,B))
print(solve2(A,B))