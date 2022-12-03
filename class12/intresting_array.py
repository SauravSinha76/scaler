def solve(A):
    ans =0
    for a in A:
        ans ^= a

    if ans & 1 == 0:
        return "Yes"
    else:
        return "No"


# A = [9, 17]
A = [1]
print(solve(A))