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

    for c in C:
        count =0
        low = 0
        high = A-1

        while low <= high:
            mid = (low + high) // 2

            if candies[mid] < c:
                low = mid +1
            else:
                count = A - mid
                high = mid -1
        ans.append(count)
    print(candies)
    return ans

A = 4
B =[[1,2],
    [4,4],
    [1,3]
    ]
C = [1,2,3]

A = 4
B = [
    [3,4],
    [2,3]
]
C =[2,2]
print(solve(A,B,C))


