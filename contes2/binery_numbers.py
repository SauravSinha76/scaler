def flip(x):
    ans = ""
    for a in x:
        if a == '1':
           ans += '0'
        else:
            ans += '1'
    return ans
def binery_sum(A,B):
    n = max(len(A), len(B))
    A = A.zfill(n)[::-1]
    B = B.zfill(n)[::-1]
    ans = ""
    i = 0
    carry = 0
    while i < n:
        x = int(A[i]) + int(B[i]) + carry

        if x == 0:
            ans += '0'
            carry = 0
        elif x == 1:
            ans += '1'
            carry = 0
        elif x == 2:
            ans += '0'
            carry = 1
        elif x == 3:
            ans += '1'
            carry = 1
        i += 1

    if carry == 1:
        ans += '1'

    return ans[::-1]

A = ["11","01"]
A = ["011","100","100"]
A = ["0111000110","0110110000"]
A.sort()
print(A)
B = 2
add =""
for i in range(len(A)):
    if i < B and A[i].startswith('0'):
        f = flip(A[i])
        A[i] = f

print(A)

for i in range(len(A)):
    add = binery_sum(add, A[i])

print(add)
