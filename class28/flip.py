def solve(A):
    n = len(A)
    v = [0] * n
    for i in range(n):
        if A[i] == '1':
            v[i] = -1
        else:
            v[i] = 1

    curr_sum =0
    max_sum = -( 1<< 31)
    start = (1 << 31) -1
    end = (1 << 31) -1
    s =0
    for i in range(n):
        curr_sum += v[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
            end = i
            start = s
        elif curr_sum < 0:
            curr_sum =0
            start = i +1

    if start == (1 << 31) -1:
        return []
    else:
        return [start +1, end +1]

A ="101010000000"
print(solve(A))
