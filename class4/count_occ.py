def solve(A,B):
    count =0
    for a in A:
        if a == B:
            count +=1
    return count


#
# A = [1, 2, 2]
# B = 2

A = [1, 2, 1]
B = 3
print(solve(A,B))