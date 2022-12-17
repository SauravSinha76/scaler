def solve(A):
    n = len(A)
    sum =0
    for i in range(n):
        a = 0
        for j in range(i,n):
            a |= A[j]
            sum += a

    return sum

def solve1(A):
    n = len(A)
    totalsubarray = n*(n+1)//2
    sum =0
    max_ele = max(A)
    pos = -1
    for i in range(31,-1,-1):
        if max_ele & 1 << i:
            pos = i
            break

    for i in range(pos+1):
        v = []
        for j in range(n):
            if not(A[j] & 1 << i):
                v.append(j)
        totalcnt = 0
        cnt =1
        for j in range(1,len(v)):
            x = v[j] - v[j-1]

            if x == 1:
                cnt += 1
            else:
                totalcnt += (cnt *(cnt+1))//2
                cnt = 1
        totalcnt += (cnt * (cnt + 1)) // 2
        sum += (1 << i) * (totalsubarray - totalcnt)
    return sum

A = [1,2,3,4,5]
# A = [7, 8, 9, 10]
print(solve(A))
print(solve1(A))