def solve(A):
    num = [True] * (A+1)
    num[0] = False
    num[1] = False

    i = 2
    while i * i <= A:
        if num[i]:
            j = i * i
            while j <= A:
                num[j] = False
                j += i
        i += 1
    ans = []
    for i in range(A+1):
        if num[i]:
            ans.append(i)

    return ans


print(solve(50))