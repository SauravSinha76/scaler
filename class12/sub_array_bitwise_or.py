def solve(A,B):
    total = int((A*(A+1))/2)
    zero_count =0
    count =0
    for i in range(A-1,-1,-1):
        if B[i] == 0:
            zero_count += 1
        else:
            count += int((zero_count*(zero_count+1))/2)
            zero_count = 0

    count += int((zero_count * (zero_count + 1)) / 2)
    return total - count

A = 7
B = [1,0,0,1,0,0,1]
print(solve(A,B))
