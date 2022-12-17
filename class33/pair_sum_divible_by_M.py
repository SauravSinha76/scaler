def solve(A,B):
    n = len(A)
    count =0
    for i in range(n):
        for j in range(i+1,n):
            if (A[i]+A[j]) % B == 0:
                count+=1
    return count % (10 **9 + 7)

def solve1(A,B):
    n = len(A)
    hm = {}
    count =0
    for i in range(n):
        A[i] %= B
        if A[i] in hm:
            hm[A[i]] += 1
        else:
            hm[A[i]] = 1

    count += (hm.get(0,0)*(hm.get(0,0) -1))//2
    if B % 2 == 0:
        count += (hm.get(B/2,0)*(hm.get(B/2,0) -1))//2
    for i in range(1,(B+1)//2):
        count += hm.get(i,0)*hm.get(B-i,0)

    return count % (10 **9 + 7)
A = [1, 2, 3, 4, 5]
B = 2
# A = [5, 17, 100, 11]
# B = 28
print(solve(A,B))