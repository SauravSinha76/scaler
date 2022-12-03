def solve(A):
    freq = {}
    for a in A:
        if a not in freq:
            freq[a] = 1
        else:
            freq[a] += 1
    count =0
    for a in freq:
        if freq[a] == 1:
            count += 1
    return count

A = [3, 4, 3, 6, 6]
print(solve(A))