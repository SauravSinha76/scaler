def solve(A):
    s = set()

    for i in range(len(A)):
        s.add(A[i])
    max_length = 1
    for i in s:
        if i -1 not in s:
            chain = 1
            val = i +1
            while val in s:
                chain += 1
                val += 1
            max_length = max(max_length,chain)
    return max_length

A = [100, 4, 200, 1, 3, 2]
A = [2, 1]
print(solve(A))


