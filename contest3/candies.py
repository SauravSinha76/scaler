import bisect


def solve(A,B,C):
    candies =[0] * A

    for b in B:
        s = b[0]-1
        e = b[1]

        candies[s] += 1
        if e < A:
            candies[e] += -1

    print(candies)
    for i in range(1,A):
        candies[i] += candies[i-1]

    candies.sort()
    ans =[]
    # bisect.bisect_left(candies,)
    for c in C:
        # count =0
        # low = 0
        # high = A-1
        #
        # while low <= high:
        #     mid = (low + high) // 2
        #
        #     if candies[mid] < c:
        #         low = mid +1
        #     else:
        #         high = mid -1

        high = bisect.bisect_left(candies,c)
        ans.append( A - high )
    print(candies)
    return ans

A = 4
B =[[1,2],
    [4,4],
    [1,3]
    ]
C = [1,2,3]

# A = 4
# B = [
#     [3,4],
#     [2,3]
# ]
# C =[2,2]C
print(solve(A,B,C))


