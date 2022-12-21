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
    count =0
    for i in range(A+1):
        l = set()
        x = i
        while x > 1:
            l.add(num[x])
            x //= num[x]
        print(f"{i}:{l}")
        if len(l) == 2:
            count += 1
    return count

A = 12
print(get_spf(A))
