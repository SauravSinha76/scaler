def solve(A):
    if A == 1 :
        return 1
    if A % 2 == 0:
        return 2 * solve(A//2) -1
    else:
        return 2 * solve(A//2) +1

def solve1(A,B):
    if A == 1:
        return 1

    return (solve1(A-1,B) + B-1) % A + 1

def solve3(A,B):
    if A ==1:
        return 0

    idx = solve3(A-1,B)

    ans = (idx + B) % A
    return ans

# def solve1(A):
#     if A == 1:
#         return 1
#
#     return (solve1(A-1) + 1)

print(solve(100))
print(solve1(2,3))
print(solve3(12,3)+1)