def is_prime(A):
    if A ==1:
        return 0
    i = 2
    while i*i <= A:
        if A % i == 0:
            return 0
        i += 1
    return 1

def solve(A):
    count =0
    for i in range(1,A+1):
        if is_prime(i):
            count += 1
    return count


print(solve(19))

