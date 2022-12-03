import functools

def factor(x):
    count =0
    i =1
    while i*i <= x:
        if x % i == 0:
            if x//i == i:
                count += 1
            else:
                count += 2
        i += 1
    return count
def compare(x , y):
    factor_x = factor(x)
    factor_y = factor(y)

    if factor_x < factor_y:
        return -1
    elif factor_x == factor_y and x < y:
        return -1
    else:
        return 1

def solve(A):
    A.sort(key=functools.cmp_to_key(compare))
    return A



A =[36, 13, 13, 26, 37, 28, 27, 43, 7]
print(solve(A))