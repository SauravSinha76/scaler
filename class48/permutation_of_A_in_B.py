def check2(hm_a, hm_b):
    for a in hm_a:
        if hm_a[a] != hm_b.get(a, 0):
            return False
    return True

def solve(A,B):
    hm_a = {}
    for i in range(len(A)):
        hm_a[A[i]] = hm_a.get(A[i], 0) + 1
    hm_b = {}
    for i in range(len(A)):
        hm_b[B[i]] = hm_b.get(B[i], 0) + 1
    count = 0
    if check2(hm_a, hm_b):
        count += 1

    start = 0
    end = len(A)

    while end < len(B):
        if hm_b.get(B[start], 0) > 0:
            hm_b[B[start]] -= 1
        hm_b[B[end]] = hm_b.get(B[end], 0) + 1
        if check2(hm_a, hm_b):
            count += 1
        start += 1
        end += 1
    return count

A = "abc"
B = "abcbacabc"
print(solve(A,B))