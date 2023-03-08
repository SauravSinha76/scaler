from math import log2


def left_and_right_subtree_nodes(A):
    h = int(log2(A))
    nodes_till_penultimate_left = (1 << (h-1)) - 1
    max_last_level_left = 1 << (h-1)
    last_level_nodes = A - (1 << h) + 1
    last_level_left = min(max_last_level_left, last_level_nodes)
    left_subtree_nodes = nodes_till_penultimate_left + last_level_left
    right_subtree_nodes = A - 1 - left_subtree_nodes
    return left_subtree_nodes, right_subtree_nodes

def ways(A):
    if A <= 2:
        return 1
    if A <= 4:
        return A-1
    left_subtree_nodes, right_subtree_nodes = left_and_right_subtree_nodes(A)
    return selecting_left(A-1, left_subtree_nodes) * ways(left_subtree_nodes) * ways(right_subtree_nodes)

def selecting_left(n, r):
    if n == r:
        return 1
    if r == 1 or r == (n-1):
        return n
    num = max(n-r, r) + 1
    den = min(n-r, r)

    for i in range(num+1, n+1):
        num *= i

    for i in range(den-1, 1, -1):
        den *= i

    return num // den

def solve(A):


    return ways(A) % (10**9 + 7)

print(solve(10))