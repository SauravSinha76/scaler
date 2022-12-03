def solve(A):
    count =0
    while A >1:
        A //=2
        count+=1
    return count

print(solve(16))