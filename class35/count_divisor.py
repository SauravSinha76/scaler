def get_spf(A):
    num = [i for i in range(A+1)]
    num[0] = -1
    num[1] = -1

    i = 2
    while i * i <= A:
        if num[i] == i:
            j = i * i
            while j <= A:
                if num[j] == j:
                    num[j] = num[i]
                j += i
        i += 1
    return num

def solve(A):
    max_ele = max(A)
    spf = get_spf(max_ele)
    n = len(A)
    ans = []
    for i in range(n):
        if A[i] == 1:
            ans.append(1)
        else:
            l =[]
            x = A[i]
            while x > 1:
                l.append(spf[x])
                x //= spf[x]
            count =1
            total_fac =1
            for k in range(1,len(l)):
                if l[k] == l[k-1]:
                    count += 1
                else:
                    total_fac *= (count +1)
                    count =1
            total_fac *= (count +1)
            ans.append(total_fac)
    return ans




A = [2, 3, 4, 5,1]
# A = [8, 9, 10]
print(solve(A))

