def recusive1(S,B):
    if B == 0:
        return S
    if S == "0":
        S= "01"
    else:
        S = "10"
    return recusive1(S[-1],B//2)

def recusive(A,S):
    if A == 0:
        return S
    ans = ""
    for s in S:
        if s == "0":
            ans += "01"
        else:
            ans += "10"
    return recusive(A-1,ans)

def solve2(A,B):
    S = "0"
    if B == 0:
        return 0
    elif B == 1:
        return 1
    else:
        return recusive1(S,B-1)

def solve4(A,B):
    if A == 1:
        return 0
    if (B+1) % 2 == 0:
        return 1 - solve4(A-1,B//2)
    else:
        return solve4(A-1,B//2)

def kthGrammar(n: int, k: int) -> int:
    if n == 1 or k == 0:
        return 0

    half = 1 << n-2
    if k >= half:
        k -= half
        return 1 - kthGrammar(n - 1, k)
    else:
        return kthGrammar(n - 1, k)

def solve3(A,B):
    if A == 0 and B == 0:
        return 0
    mid = pow(2,A-1)//2
    print(mid)
    if B <= mid:
        return solve3(A-1,B)
    else:
        return 1- solve3(A-1,B-mid)

def solve1(A,B):
    S = "0"
    S = recusive(A-1,S)
    print(S)
    return S[B]

def solve(A,B):
    S = "0"
    while A > 0:
        ans = ""
        for s in S:
            if s == "0":
               ans += "01"
            else:
                ans += "10"
        S = ans
        A -= 1

    return S[B]

def solve5(A,B):
    if B == 0:
        return 0
    val = solve5(A-1, B//2)
    if B % 2 == 0:
        return val
    else:
        return 1 - val
A = 9
B = 239
print(solve(A,B))
# print(solve1(A,B))
# print(solve3(A,B))
print(kthGrammar(A,B))
print(solve5(A,B))

