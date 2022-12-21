def get_spf(A):
    num = [i for i in range(A+1)]
    num[0] = 0

    i = 2
    while i * i <= A:
        if num[i] == i:
            j = i * i
            while j <= A:
                if num[j] == j:
                    num[j] = num[i]
                j += i
        i += 1
    prv_prim = 3
    for i in range(A+1):
        if num[i] == i:
            prv_prim = num[i]
        else:
            num[i] = prv_prim
    return num

def unique_prime_factor(A,prime_fact):
    l =set()
    x = A
    for i in range(A):
        if prime_fact[i] == i:
            l.add(i)
        else:
            while x > 1:
                l.add(prime_fact[x])
                x //=prime_fact[x]
    print(f"{A}:{l}")
    return sum(l)

def solve2(A):
    prime_fact = get_spf(max(A))
    n = len(A)
    freq = {}

    hm ={1:{1}}
    for i in range(2,max(A)+1):
        l = set()
        if prime_fact[i] == i:
            l.add(i)
        else:
            x = i
            while x > 1:
                l.add(prime_fact[x])
                x //= prime_fact[x]
        previous = hm.get(i-1)
        hm[i] = l.union(previous)
    print(hm)
    for i in range(n):
        if A[i] != 1:
            print(F"{A[i]}: {unique_prime_factor(A[i],prime_fact)}")
            A[i] = sum(hm[A[i]])
            freq[A[i]] = freq.get(A[i], 0) + 1

    sub_sqenc_count = 0
    for f in freq.values():
        sub_sqenc_count += 2 ** f - 1
    return sub_sqenc_count
def solve(A):
    prime_fact = get_spf(max(A))
    print(prime_fact)
    n = len(A)
    freq ={}
    for i in range(n):
        if A[i] != 1:
            A[i] = prime_fact[A[i]]
            freq[A[i]] = freq.get(A[i],0) +1
    sub_sqenc_count =0
    for f in freq.values():
        sub_sqenc_count += 2 ** f -1
    return sub_sqenc_count
A =[2,3,2,3]
A = [2, 3, 4]
print(solve(A))
