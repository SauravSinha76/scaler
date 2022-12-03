def solve(A,B):
    freq = {}
    ans =[]
    for a in A:
        if a not in freq:
            freq[a] = 1
        else:
            freq[a] += 1
    for b in B:
        if b in freq and freq[b] > 0:
            ans.append(b)
            freq[b] -= 1
    return ans

A = [1, 2, 2, 1]
B = [2, 3, 1, 2]
print(solve(A,B))

