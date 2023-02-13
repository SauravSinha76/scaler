def get_max_xor(A):
    stack, max_xor = [], 0
    for x in A:
        while len(stack) != 0 and x > stack[-1]:
            stack.pop()

        if len(stack) > 1:
            max_xor = max(max_xor, stack[-1]^stack[-2])

        else:
            stack.append(x)
    return max_xor

# @param A : list of integers
# @return an integer
def solve( A):
    max_xor_left = get_max_xor(A)
    # reverse the array to get the xor of elements from right to left, i.e in reverse order
    A.reverse()
    max_xor_right = get_max_xor(A)

    return max(max_xor_left, max_xor_right)

A = [2, 3, 1, 4]
print(solve(A))