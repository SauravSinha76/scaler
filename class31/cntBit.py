def f(A,B):
    count =0
    res = A ^ B
    for i in range(31,-1,-1):
        if res >> i & 1:
            count += 1
    return count

def solve(A):
    n = len(A)
    cont = 0
    for i in range(n):
        for j in range(i+1,n):
            cont += 2 * f(A[i],A[j])
    return cont


def solve1(arr):
    ans = 0  # Initialize result
    n = len(arr)
    # traverse over all bits
    for i in range(31):

        # count number of elements with i'th bit set
        count = 0
        for j in range(n):
            if arr[j] & (1 << i):
                count += 1

        # Add "count * (n - count) * 2" to the answer
        ans += (count * (n - count) * (1 << i))

    return ans * 2
A = [1, 3, 5]
A = [1,2, 3]
A = [2,3,5,6,8]
print(solve(A))
print(solve1(A))