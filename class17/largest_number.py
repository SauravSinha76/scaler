import functools

def compare(x,y):
    xy = str(x)+str(y)
    yx = str(y)+str(x)

    if int(xy) > int(yx):
        return 1
    else:
        return -1


def solve(A):
    A = tuple(A)
    B = sorted(A, key=functools.cmp_to_key(compare),reverse=True)
    ans = ""
    for a in B:
        if ans != "0" or a != 0:
            ans += str(a)
    return ans


A = [0,0,0,0]
A = [3, 30, 34, 5, 9]
print(solve(A))
print("30" == "3")
