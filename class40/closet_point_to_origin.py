import functools
import math


def euclidean_distant(x):
    return math.sqrt(x[0] ** 2 + x[1] ** 2)

def compare(x , y):
    distance_x = euclidean_distant(x)
    distance_y = euclidean_distant(y)

    if distance_x < distance_y:
        return -1
    elif distance_x == distance_y:
        return -1
    else:
        return 1

def solve(A,B):
    A.sort(key=functools.cmp_to_key(compare))
    return A[:B]

A = [
       [1, 3],
       [-2, 2]
     ]
B = 1

# A = [
#     [1, -1],
#     [2, -1]
# ]
# B = 1
print(solve(A,B))